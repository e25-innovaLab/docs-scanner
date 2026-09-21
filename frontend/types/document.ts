export interface Document {
  id: string;
  name: string;
  type: 'pdf' | 'text';
  content: string;
  pages?: number;
  uploadedAt: Date;
}

export interface TextDocument extends Document {
  type: 'text';
  wordCount: number;
}

export interface PdfDocument extends Document {
  type: 'pdf';
  pages: number;
  hasStructure: boolean;
}
