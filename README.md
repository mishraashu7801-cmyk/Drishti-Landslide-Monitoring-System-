# DRISHTI-NER: Landslide Early Warning & Telemetry System

> **Disaster Risk Intelligence & Slope Hazard Telemetry (8 North Eastern States of India)**  
> Production-grade, multi-hazard early warning GIS platform engineered for Assam, Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, and Tripura.

---

## 🚀 Quick Start Guide

### Prerequisites
- **Node.js**: v20.0.0 or higher ([Download Node.js](https://nodejs.org/))
- **npm** (comes with Node.js) or **pnpm** / **yarn** / **bun**

### 1. Installation
Extract the zip file to your preferred folder and install the dependencies:

```bash
# Navigate to the project directory
cd drishti-ner

# Install dependencies
npm install
```

### 2. Environment Setup (Optional)
If you wish to use Google Gemini AI features for real-time SITREP and multimodal photo damage analysis:

```bash
# Copy example environment configuration
cp .env.example .env

# Edit .env and supply your Gemini API Key:
# GEMINI_API_KEY="your-api-key-here"
```
*(The application runs fully in client-mode with comprehensive synthetic telemetry even without an API key).*

### 3. Run Development Server
```bash
npm run dev
```
Open your browser at: **`http://localhost:3000`**

### 4. Build for Production
To create an optimized production build:
```bash
npm run build
```
The compiled static assets will be in the `dist/` directory. You can preview the production build locally with:
```bash
npm run preview
```

---

## 🐳 Docker Deployment (Zero-Config)

If you prefer to run with Docker:

```bash
# Build and run container
docker compose up --build
```
Access the application at `http://localhost:3000`.

To build and run manually with standard Docker:
```bash
docker build -t drishti-ner .
docker run -p 3000:3000 drishti-ner
```

---

## 📦 Project Structure

```text
├── public/                     # Static assets, PWA icons, manifest, PDFs & downloads
│   ├── DRISHTI_NER_Architecture_Specification.pdf # Complete system architecture specification
│   ├── drishti-ner-source-code.zip                # Complete portable source package
│   ├── pwa-192x192.png, pwa-512x512.png           # PWA progressive web app icons
│   └── favicon.png, icon.svg                      # Brand icons
├── src/
│   ├── components/             # React 19 UI & GIS components
│   │   ├── MapQGISView.tsx     # Leaflet interactive map with Survey of India boundary lock
│   │   ├── Navbar.tsx          # Top navigation, multilingual selector & action buttons
│   │   ├── DashboardOverview.tsx # Real-time state-by-state risk overview & telemetry
│   │   ├── TelemetryPanel.tsx  # InSAR, NASA GPM & SMAP sensor telemetry
│   │   ├── RoadConnectivityBoard.tsx # NH-2, NH-29, NH-10 real-time highway corridors
│   │   ├── CitizenIncidentReporting.tsx # Field incident crowdsourcing with photo upload
│   │   ├── TechnicalDocumentationModal.tsx # 5-pillar technical specification dialog
│   │   ├── EvacuationRouteTrajectoryModal.tsx # Offline vector evacuation maps
│   │   ├── HelplineDirectory.tsx # 24x7 SDRF, NDRF & district emergency control rooms
│   │   └── VoiceAlertModal.tsx # Multilingual voice siren configuration
│   ├── data/                   # Geospatial boundaries, state matrices & historical records
│   │   ├── nerData.ts          # WGS84 coordinates & geological fault line vectors
│   │   ├── languages.ts        # 28 regional languages & phonetic emergency translations
│   │   └── historicalLandslides.ts # Historical landslide catalog & rainfall thresholds
│   ├── services/               # Modular application services
│   │   ├── voiceAlertService.ts # Web Speech API voice synthesis
│   │   ├── authService.ts      # Multi-role authentication & session state
│   │   ├── citizenService.ts   # Incident submissions & verification workflow
│   │   └── notificationService.ts # Push alerts & siren triggers
│   ├── hooks/                  # React custom hooks
│   │   └── usePWAInstall.ts    # Progressive web app install prompt handler
│   ├── App.tsx                 # Root application controller
│   ├── main.tsx                # React DOM entry point
│   ├── types.ts                # TypeScript strict interface definitions
│   └── index.css               # Tailwind CSS v4 styling & print media styles
├── scripts/
│   ├── generate_pdf.js         # Headless PDF generation script via jsPDF
│   ├── generate-icons.cjs      # PWA icon generator script
│   └── package_zip.py          # Python source packager script
├── package.json                # Project dependencies and npm scripts
├── tsconfig.json               # TypeScript compiler configuration
├── vite.config.ts              # Vite configuration with PWA plugin
└── Dockerfile                  # Production container definition
```

---

## 🛠️ Key Technologies

- **Frontend**: React 19, TypeScript, Vite 8, Tailwind CSS v4, Lucide React, Motion 12
- **GIS Engine**: Leaflet 1.9, OpenStreetMap / CartoDB tiles with Survey of India boundary lock
- **Voice System**: Web Speech API supporting 28 North-Eastern languages and dialects
- **Offline / PWA**: Service worker caching with `vite-plugin-pwa`
- **PDF Generation**: Headless programmatic PDF generation via `jspdf`
- **Containerization**: Docker multi-stage build running Node.js / Nginx

---

## 📄 License & Attribution

Designed and engineered for Disaster Management Authorities, State Disaster Response Forces (SDRF), and North Eastern Region communities across India.
