import { Finding } from './diagnosis';

export type AdaptationType =
  | 'simplify'
  | 'restructure'
  | 'divide_steps'
  | 'alt_text'
  | 'improve_structure';

export type AdaptationStatus = 'pending' | 'accepted' | 'edited' | 'rejected';

export interface Adaptation {
  id: string;
  findingId: string;
  original: string;
  proposed: string;
  type: AdaptationType;
  status: AdaptationStatus;
}

export interface AdaptationSummary {
  total: number;
  accepted: number;
  edited: number;
  rejected: number;
  pending: number;
}
