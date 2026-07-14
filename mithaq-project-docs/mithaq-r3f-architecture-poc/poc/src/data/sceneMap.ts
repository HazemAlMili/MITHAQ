export interface MithaqSceneMapItem {
  id: number;
  label: string;
  start: number;
  end: number;
}

export const MITHAQ_SCENE_MAP: MithaqSceneMapItem[] = [
  { id: 1, label: 'Gavel Seal Opening', start: 0.00, end: 0.10 },
  { id: 2, label: 'Hero / Mithaq Reveal', start: 0.10, end: 0.22 },
  { id: 3, label: 'The Gap', start: 0.22, end: 0.37 },
  { id: 4, label: 'The Mithaq Method', start: 0.37, end: 0.50 },
  { id: 5, label: 'Training Pillars', start: 0.50, end: 0.62 },
  { id: 6, label: 'Workshops Preview', start: 0.62, end: 0.72 },
  { id: 7, label: 'Hall of Mentors', start: 0.72, end: 0.82 },
  { id: 8, label: 'Trust & Credibility', start: 0.82, end: 0.88 },
  { id: 9, label: 'FAQ', start: 0.88, end: 0.94 },
  { id: 10, label: 'Final CTA', start: 0.94, end: 1.00 }
];

export function getSceneByProgress(progress: number): MithaqSceneMapItem {
  return MITHAQ_SCENE_MAP.find((scene) => progress >= scene.start && progress < scene.end) ?? MITHAQ_SCENE_MAP[9];
}
