# auto-generated file
import _cffi_backend

ffi = _cffi_backend.FFI('ocrmypdf.lib._leptonica',
    _version = 0x2601,
    _types = b'\x00\x00\x01\x0D\x00\x01\x56\x03\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x01\x57\x03\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x01\x5B\x03\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x01\x5D\x03\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x01\x5C\x03\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x04\x0D\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x09\x03\x00\x00\x18\x11\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x01\x58\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x01\x11\x00\x00\x01\x03\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x18\x11\x00\x00\x05\x03\x00\x00\x11\x11\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x0D\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x01\x61\x03\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x0D\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x0D\x01\x00\x00\x2A\x11\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x0D\x01\x00\x00\x2A\x11\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x0D\x01\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x00\x11\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x01\x64\x03\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x01\x76\x03\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x09\x0D\x00\x01\x78\x03\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x11\x0D\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x01\x5F\x0D\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x01\x5F\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x01\x5F\x0D\x00\x00\x11\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\xA4\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x4D\x0D\x00\x00\x92\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x92\x11\x00\x00\x00\x0F\x00\x00\x4D\x0D\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x01\x63\x0D\x00\x00\x4D\x11\x00\x00\x00\x0F\x00\x01\x63\x0D\x00\x00\x00\x0F\x00\x00\x2A\x0D\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x1C\x11\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x1C\x11\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x09\x11\x00\x00\x04\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x3A\x03\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x2A\x11\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x09\x11\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\xD6\x11\x00\x00\xD6\x11\x00\x00\xD6\x11\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x09\x11\x00\x00\xD6\x11\x00\x00\xD6\x11\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x09\x11\x00\x00\x2A\x11\x00\x00\x2A\x11\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x0D\x01\x00\x00\x07\x01\x00\x00\x2A\x11\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x01\x59\x03\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\xD6\x11\x00\x00\xD6\x11\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x0D\x01\x00\x00\x18\x11\x00\x00\x18\x11\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x09\x11\x00\x01\x77\x03\x00\x00\x96\x03\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x92\x11\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x92\x11\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\xFF\x11\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x92\x11\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x01\x75\x03\x00\x01\x17\x11\x00\x00\x09\x11\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x01\x2C\x11\x00\x01\x17\x11\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x05\x0D\x00\x01\x2C\x11\x00\x01\x17\x11\x00\x00\x09\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x01\x7B\x0D\x00\x00\x25\x11\x00\x00\x00\x0F\x00\x01\x7B\x0D\x00\x00\x04\x03\x00\x00\x00\x0F\x00\x01\x7B\x0D\x00\x00\xFF\x11\x00\x00\x00\x0F\x00\x01\x7B\x0D\x00\x00\x18\x11\x00\x00\x00\x0F\x00\x01\x7B\x0D\x00\x00\x11\x03\x00\x00\x00\x0F\x00\x01\x7B\x0D\x00\x00\xA4\x11\x00\x00\x00\x0F\x00\x01\x7B\x0D\x00\x00\x4D\x03\x00\x00\x00\x0F\x00\x01\x7B\x0D\x00\x01\x7B\x03\x00\x00\x00\x0F\x00\x00\x00\x09\x00\x00\x01\x09\x00\x00\x0A\x09\x00\x01\x5A\x03\x00\x00\x02\x09\x00\x00\x03\x09\x00\x00\x06\x09\x00\x00\x07\x09\x00\x00\x04\x09\x00\x01\x60\x03\x00\x00\x08\x09\x00\x00\x09\x09\x00\x01\x63\x03\x00\x01\x64\x03\x00\x00\x02\x01\x00\x00\x0E\x01\x00\x00\x00\x0B\x00\x00\x01\x0B\x00\x00\x02\x0B\x00\x00\x03\x0B\x00\x00\x04\x0B\x00\x00\x05\x0B\x00\x00\x06\x0B\x00\x00\x2A\x03\x00\x00\x0B\x01\x00\x00\x05\x01\x00\x00\x03\x01\x00\x01\x5E\x03\x00\x01\x73\x03\x00\x01\x74\x03\x00\x00\x05\x09\x00\x01\x76\x03\x00\x00\x04\x01\x00\x01\x78\x03\x00\x00\x08\x01\x00\x00\x0C\x01\x00\x00\x06\x01\x00\x00\x00\x01',
    _globals = (b'\xFF\xFF\xFF\x0BL_BF_ANY',1,b'\xFF\xFF\xFF\x0BL_BF_CODABAR',9,b'\xFF\xFF\xFF\x0BL_BF_CODE128',2,b'\xFF\xFF\xFF\x0BL_BF_CODE2OF5',5,b'\xFF\xFF\xFF\x0BL_BF_CODE39',7,b'\xFF\xFF\xFF\x0BL_BF_CODE93',8,b'\xFF\xFF\xFF\x0BL_BF_CODEI2OF5',6,b'\xFF\xFF\xFF\x0BL_BF_EAN13',4,b'\xFF\xFF\xFF\x0BL_BF_EAN8',3,b'\xFF\xFF\xFF\x0BL_BF_UNKNOWN',0,b'\xFF\xFF\xFF\x0BL_BF_UPCA',10,b'\xFF\xFF\xFF\x0BL_CLONE',2,b'\xFF\xFF\xFF\x0BL_COPY',1,b'\xFF\xFF\xFF\x0BL_COPY_CLONE',3,b'\xFF\xFF\xFF\x0BL_DEFAULT_ENCODE',0,b'\xFF\xFF\xFF\x0BL_FLATE_ENCODE',3,b'\xFF\xFF\xFF\x0BL_G4_ENCODE',2,b'\xFF\xFF\xFF\x0BL_INSERT',0,b'\xFF\xFF\xFF\x0BL_JP2K_ENCODE',4,b'\xFF\xFF\xFF\x0BL_JPEG_ENCODE',1,b'\xFF\xFF\xFF\x0BL_NOCOPY',0,b'\xFF\xFF\xFF\x0BL_SEVERITY_ALL',1,b'\xFF\xFF\xFF\x0BL_SEVERITY_DEBUG',2,b'\xFF\xFF\xFF\x0BL_SEVERITY_ERROR',5,b'\xFF\xFF\xFF\x0BL_SEVERITY_EXTERNAL',0,b'\xFF\xFF\xFF\x0BL_SEVERITY_INFO',3,b'\xFF\xFF\xFF\x0BL_SEVERITY_NONE',6,b'\xFF\xFF\xFF\x0BL_SEVERITY_WARNING',4,b'\xFF\xFF\xFF\x0BL_USE_WIDTHS',1,b'\xFF\xFF\xFF\x0BL_USE_WINDOWS',2,b'\xFF\xFF\xFF\x0BREMOVE_CMAP_BASED_ON_SRC',4,b'\xFF\xFF\xFF\x0BREMOVE_CMAP_TO_BINARY',0,b'\xFF\xFF\xFF\x0BREMOVE_CMAP_TO_FULL_COLOR',2,b'\xFF\xFF\xFF\x0BREMOVE_CMAP_TO_GRAYSCALE',1,b'\xFF\xFF\xFF\x0BREMOVE_CMAP_WITH_ALPHA',3,b'\xFF\xFF\xFF\x0BSEL_DONT_CARE',0,b'\xFF\xFF\xFF\x0BSEL_HIT',1,b'\xFF\xFF\xFF\x0BSEL_MISS',2,b'\x00\x00\x00\x23boxClone',0,b'\x00\x01\x3E\x23boxDestroy',0,b'\x00\x01\x41\x23boxaDestroy',0,b'\x00\x00\x03\x23boxaGetBox',0,b'\x00\x01\x19\x23getImpliedFileFormat',0,b'\x00\x00\xBE\x23getLeptonicaVersion',0,b'\x00\x01\x44\x23l_CIDataDestroy',0,b'\x00\x01\x1C\x23l_generateCIDataForPdf',0,b'\x00\x01\x53\x23lept_free',0,b'\x00\x00\xC0\x23makePixelSumTab8',0,b'\x00\x00\x31\x23pixAnd',0,b'\x00\x00\x3E\x23pixBackgroundNorm',0,b'\x00\x00\x36\x23pixCleanBackgroundToWhite',0,b'\x00\x00\x22\x23pixClipRectangle',0,b'\x00\x01\x01\x23pixColorFraction',0,b'\x00\x00\x85\x23pixColorMagnitude',0,b'\x00\x00\x1F\x23pixConvertRGBToLuminance',0,b'\x00\x00\x7C\x23pixConvertTo8',0,b'\x00\x00\xD3\x23pixCorrelationBinary',0,b'\x00\x00\xED\x23pixCountPixels',0,b'\x00\x00\x98\x23pixDeserializeFromMemory',0,b'\x00\x00\x7C\x23pixDeskew',0,b'\x00\x01\x47\x23pixDestroy',0,b'\x00\x00\x4A\x23pixDilate',0,b'\x00\x00\x1F\x23pixEndianByteSwapNew',0,b'\x00\x00\xD8\x23pixEqual',0,b'\x00\x00\x4A\x23pixErode',0,b'\x00\x00\x9C\x23pixExtractBarcodes',0,b'\x00\x00\x08\x23pixFindPageForeground',0,b'\x00\x00\xE8\x23pixFindSkew',0,b'\x00\x00\x4F\x23pixGammaTRC',0,b'\x00\x00\x27\x23pixGenHalftoneMask',0,b'\x00\x00\xFA\x23pixGenerateCIData',0,b'\x00\x00\xDD\x23pixGetAverageMaskedRGB',0,b'\x00\x00\x56\x23pixGlobalNormRGB',0,b'\x00\x00\x4A\x23pixHMT',0,b'\x00\x00\x2D\x23pixInvert',0,b'\x00\x00\x15\x23pixLocateBarcodes',0,b'\x00\x00\x80\x23pixMaskOverColorPixels',0,b'\x00\x00\x5E\x23pixMaskedThreshOnBackgroundNorm',0,b'\x00\x00\xF2\x23pixNumSignificantGrayColors',0,b'\x00\x01\x0A\x23pixOtsuAdaptiveThreshold',0,b'\x00\x00\x6A\x23pixOtsuThreshOnBackgroundNorm',0,b'\x00\x00\xA0\x23pixProcessBarcodes',0,b'\x00\x00\x91\x23pixRead',0,b'\x00\x00\xA7\x23pixReadBarcodes',0,b'\x00\x00\x94\x23pixReadMem',0,b'\x00\x00\x1B\x23pixReadStream',0,b'\x00\x00\x7C\x23pixRemoveColormap',0,b'\x00\x00\x80\x23pixRemoveColormapGeneral',0,b'\x00\x00\xCD\x23pixRenderBoxa',0,b'\x00\x00\x2D\x23pixRotate180',0,b'\x00\x00\x7C\x23pixRotateOrth',0,b'\x00\x00\x77\x23pixScale',0,b'\x00\x01\x14\x23pixSerializeToMemory',0,b'\x00\x00\x31\x23pixSubtract',0,b'\x00\x01\x22\x23pixWriteImpliedFormat',0,b'\x00\x01\x31\x23pixWriteMem',0,b'\x00\x01\x37\x23pixWriteMemJpeg',0,b'\x00\x01\x2B\x23pixWriteMemPng',0,b'\x00\x00\xC2\x23pixWriteStream',0,b'\x00\x00\xC7\x23pixWriteStreamJpeg',0,b'\x00\x01\x4A\x23pixaDestroy',0,b'\x00\x00\x10\x23pixaGetBox',0,b'\x00\x00\x8C\x23pixaGetPix',0,b'\x00\x01\x4D\x23sarrayDestroy',0,b'\x00\x00\xB4\x23selCreateBrick',0,b'\x00\x00\xAE\x23selCreateFromString',0,b'\x00\x01\x50\x23selDestroy',0,b'\x00\x00\xBB\x23selPrintToString',0,b'\x00\x01\x28\x23setMsgSeverity',0),
    _struct_unions = ((b'\x00\x00\x01\x56\x00\x00\x00\x02Box',b'\x00\x00\x05\x11x',b'\x00\x00\x05\x11y',b'\x00\x00\x05\x11w',b'\x00\x00\x05\x11h',b'\x00\x01\x78\x11refcount'),(b'\x00\x00\x01\x57\x00\x00\x00\x02Boxa',b'\x00\x00\x05\x11n',b'\x00\x00\x05\x11nalloc',b'\x00\x01\x78\x11refcount',b'\x00\x00\x25\x11box'),(b'\x00\x00\x01\x5A\x00\x00\x00\x02L_Compressed_Data',b'\x00\x00\x05\x11type',b'\x00\x01\x75\x11datacomp',b'\x00\x00\x96\x11nbytescomp',b'\x00\x01\x63\x11data85',b'\x00\x00\x96\x11nbytes85',b'\x00\x01\x63\x11cmapdata85',b'\x00\x01\x63\x11cmapdatahex',b'\x00\x00\x05\x11ncolors',b'\x00\x00\x05\x11w',b'\x00\x00\x05\x11h',b'\x00\x00\x05\x11bps',b'\x00\x00\x05\x11spp',b'\x00\x00\x05\x11minisblack',b'\x00\x00\x05\x11predictor',b'\x00\x00\x96\x11nbytes',b'\x00\x00\x05\x11res'),(b'\x00\x00\x01\x5B\x00\x00\x00\x02Pix',b'\x00\x01\x78\x11w',b'\x00\x01\x78\x11h',b'\x00\x01\x78\x11d',b'\x00\x01\x78\x11spp',b'\x00\x01\x78\x11wpl',b'\x00\x01\x78\x11refcount',b'\x00\x00\x05\x11xres',b'\x00\x00\x05\x11yres',b'\x00\x00\x05\x11informat',b'\x00\x00\x05\x11special',b'\x00\x01\x63\x11text',b'\x00\x01\x71\x11colormap',b'\x00\x01\x77\x11data'),(b'\x00\x00\x01\x5E\x00\x00\x00\x02PixColormap',b'\x00\x01\x54\x11array',b'\x00\x00\x05\x11depth',b'\x00\x00\x05\x11nalloc',b'\x00\x00\x05\x11n'),(b'\x00\x00\x01\x74\x00\x00\x00\x10PixComp',),(b'\x00\x00\x01\x5C\x00\x00\x00\x02Pixa',b'\x00\x00\x05\x11n',b'\x00\x00\x05\x11nalloc',b'\x00\x01\x78\x11refcount',b'\x00\x00\x18\x11pix',b'\x00\x00\x04\x11boxa'),(b'\x00\x00\x01\x5D\x00\x00\x00\x02PixaComp',b'\x00\x00\x05\x11n',b'\x00\x00\x05\x11nalloc',b'\x00\x00\x05\x11offset',b'\x00\x01\x72\x11pixc',b'\x00\x00\x04\x11boxa'),(b'\x00\x00\x01\x60\x00\x00\x00\x02Sarray',b'\x00\x00\x05\x11nalloc',b'\x00\x00\x05\x11n',b'\x00\x00\x05\x11refcount',b'\x00\x01\x62\x11array'),(b'\x00\x00\x01\x61\x00\x00\x00\x02Sel',b'\x00\x00\x05\x11sy',b'\x00\x00\x05\x11sx',b'\x00\x00\x05\x11cy',b'\x00\x00\x05\x11cx',b'\x00\x01\x6D\x11data',b'\x00\x01\x63\x11name'),(b'\x00\x00\x01\x58\x00\x00\x00\x10_IO_FILE',)),
    _enums = (b'\x00\x00\x01\x66\x00\x00\x00\x16$1\x00L_DEFAULT_ENCODE,L_JPEG_ENCODE,L_G4_ENCODE,L_FLATE_ENCODE,L_JP2K_ENCODE',b'\x00\x00\x01\x67\x00\x00\x00\x16$2\x00REMOVE_CMAP_TO_BINARY,REMOVE_CMAP_TO_GRAYSCALE,REMOVE_CMAP_TO_FULL_COLOR,REMOVE_CMAP_WITH_ALPHA,REMOVE_CMAP_BASED_ON_SRC',b'\x00\x00\x01\x68\x00\x00\x00\x16$3\x00L_NOCOPY,L_INSERT,L_COPY,L_CLONE,L_COPY_CLONE',b'\x00\x00\x01\x69\x00\x00\x00\x16$4\x00L_USE_WIDTHS,L_USE_WINDOWS',b'\x00\x00\x01\x6A\x00\x00\x00\x16$5\x00L_BF_UNKNOWN,L_BF_ANY,L_BF_CODE128,L_BF_EAN8,L_BF_EAN13,L_BF_CODE2OF5,L_BF_CODEI2OF5,L_BF_CODE39,L_BF_CODE93,L_BF_CODABAR,L_BF_UPCA',b'\x00\x00\x01\x6B\x00\x00\x00\x16$6\x00L_SEVERITY_EXTERNAL,L_SEVERITY_ALL,L_SEVERITY_DEBUG,L_SEVERITY_INFO,L_SEVERITY_WARNING,L_SEVERITY_ERROR,L_SEVERITY_NONE',b'\x00\x00\x01\x6C\x00\x00\x00\x16$7\x00SEL_DONT_CARE,SEL_HIT,SEL_MISS'),
    _typenames = (b'\x00\x00\x01\x56BOX',b'\x00\x00\x01\x57BOXA',b'\x00\x00\x01\x58FILE',b'\x00\x00\x01\x5AL_COMP_DATA',b'\x00\x00\x01\x5BPIX',b'\x00\x00\x01\x5CPIXA',b'\x00\x00\x01\x5DPIXAC',b'\x00\x00\x01\x5EPIXCMAP',b'\x00\x00\x01\x60SARRAY',b'\x00\x00\x01\x61SEL',b'\x00\x00\x00\x3Al_float32',b'\x00\x00\x01\x65l_float64',b'\x00\x00\x01\x6Fl_int16',b'\x00\x00\x00\x05l_int32',b'\x00\x00\x01\x6El_int64',b'\x00\x00\x01\x70l_int8',b'\x00\x00\x00\x05l_ok',b'\x00\x00\x01\x7Al_uint16',b'\x00\x00\x01\x78l_uint32',b'\x00\x00\x01\x79l_uint64',b'\x00\x00\x01\x76l_uint8'),
)
