const BASE_API_URL = import.meta.env.VITE_API_BASE_URL || 'https://sasl-perplexity-1-backend.onrender.com';

export type UploadVideoDto = {
  title: string;
  grade_level: string;
  storage_url: string;
  duration_sec: number;
  is_published: boolean;
};

export async function uploadVideoToBackend(
  dto: UploadVideoDto
): Promise<{
  id: string;
  title: string;
  grade_level: string;
  language: string;
  is_published: boolean;
  storage_url: string;
  duration_sec: number;
}> {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 30000);

  try {
    console.log('[Upload] POST', `${BASE_API_URL}/videos/upload`, dto);
    const response = await fetch(`${BASE_API_URL}/videos/upload`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dto),
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      const text = await response.text();
      console.error('[Upload] Backend error:', response.status, text);
      throw new Error(`Backend error (${response.status}): ${text}`);
    }

    const data = await response.json();
    console.log('[Upload] Success:', data);
    return data;
  } catch (err) {
    clearTimeout(timeoutId);
    if (err instanceof DOMException && err.name === 'AbortError') {
      throw new Error('Backend request timed out after 30 seconds. The server may be starting up — please try again.');
    }
    throw err;
  }
}
