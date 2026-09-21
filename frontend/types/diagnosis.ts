export type SeverityLevel = 'correct' | 'to_review' | 'barrier';

export type Dimension =
  | 'comprehension'
  | 'structure'
  | 'visual'
  | 'alternatives'
  | 'multimedia'
  | 'navigation';

export type FindingSource = 'rule' | 'ai' | 'hybrid';

export interface FindingLocation {
  page?: number;
  paragraph?: number;
  range?: [number, number];
}

export interface Finding {
  id: string;
  dimension: Dimension;
  severity: SeverityLevel;
  fragment: string;
  explanation: string;
  recommendation: string;
  source: FindingSource;
  location?: FindingLocation;
}

export interface Diagnosis {
  documentId: string;
  score: number;
  findings: Finding[];
  evaluatedCriteria: number;
  totalCriteria: number;
  isComplete: boolean;
}
