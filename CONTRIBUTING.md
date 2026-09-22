# Contributing

Conventions for everything that goes into this repository.

## Language

Everything produced for the project is written in English: commit messages, branch names, pull request titles and descriptions, code (identifiers, file names, constants), tests (`describe` / `it` strings) and technical documentation.

Two exceptions: copy shown to the end user, and the planning documents under `docs/`, are written in Spanish because the whole team reads them.

## Fallbacks and defaults

A default value is defined once, at the point where the data enters the application: state initialization or normalization of data at its source (for example, an API response). The rest of the code trusts that the value exists.

Spreading fallbacks across hooks and components (`value || 'default'` everywhere) hides missing data and makes bugs harder to find.

## Code quality

- Code is self-explanatory. Do not add comments; if a piece of code needs one, rename or restructure it instead.
- No quick and dirty solutions. Code must be maintainable and understandable by the rest of the team.

## Frontend (TypeScript)

- Never use `any`. It disables the type checker.
- Never use `unknown`. Type the value explicitly; if the type is not known, find out.
- Never use `as` to force a type. `value as User` lies to the compiler when the value has not been verified; narrow it with a type guard instead. The only allowed form is `as const`.
- Nothing is left untyped.
- Closed sets of values are declared as a `const` object and the type is derived from it (`SEVERITY_LEVEL` / `SeverityLevel`). Never a bare string union.

## UI primitives (shadcn/ui)

Buttons, inputs, cards, badges and the like come from shadcn/ui. Do not write your own.

- Use what is already in `frontend/src/components/ui/`.
- Need another primitive? Run `npx shadcn@latest add <name>` inside `frontend/` and commit the generated file. Check with `npx shadcn@latest docs <name>` how it is used.
- Do not edit generated files under `components/ui/` unless the change is meant for every screen. Compose them inside your feature instead.
- Colors, spacing and radius come from the theme tokens in `globals.css` (`bg-background`, `text-muted-foreground`, `border-border`). No ad-hoc hex values.

## Working in parallel

Each module has an owner and a folder. Nobody edits another module's folder.

| Area | Owner |
| --- | --- |
| `src/types/`, `src/fixtures/`, `package.json` | Contract owner (Task 0) |
| `src/app/layout.tsx`, `src/app/globals.css`, `src/app/page.tsx` | Upload and shell (F1) |
| `src/features/upload/` | F1 |
| `src/features/diagnosis/`, `src/app/diagnosis/` | F2 |
| `src/features/adaptation/`, `src/app/adaptation/` | F3 |

- Shared files (`types`, `fixtures`, `layout`, `globals.css`, `package.json`) change only through a pull request labeled `contract`, reviewed by the other two owners.
- One branch per task: `feat/f2-diagnosis-summary`. Small pull requests, one reviewer, rebase on `main` daily.
- Each feature exposes one entry component that receives its data through props. Pages wire fixture to component. Integration replaces the fixture; components stay untouched.
- No global state before integration (milestone B). How a document travels between routes is decided then, by whoever coordinates that milestone.
