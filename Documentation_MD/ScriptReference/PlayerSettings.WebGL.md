[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# WebGL

class in UnityEditor

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

### Description

WebGL specific player settings.

### Static Properties

[closeOnQuit](PlayerSettings.WebGL-closeOnQuit.html)| If enabled, the Unity
Player will close the browser running it when the application quits.  
---|---  
[compressionFormat](PlayerSettings.WebGL-compressionFormat.html)|
CompressionFormat defines the compression type that the WebGL resources are
encoded to.  
[dataCaching](PlayerSettings.WebGL-dataCaching.html)| Enables automatic
caching of unityweb files.  
[debugSymbolMode](PlayerSettings.WebGL-debugSymbolMode.html)| Enables
generation of debug symbols file in the build output directory. Supported
options: embedded debug symbols and debug symbols in external file.  
[decompressionFallback](PlayerSettings.WebGL-decompressionFallback.html)|
Include decompression fallback code for build files in the loader.  
[exceptionSupport](PlayerSettings.WebGL-exceptionSupport.html)| Exception
support for WebGL builds.  
[geometricMemoryGrowthStep](PlayerSettings.WebGL-
geometricMemoryGrowthStep.html)| Heap memory growth factor.  
[initialMemorySize](PlayerSettings.WebGL-initialMemorySize.html)| Initial size
of the WASM heap memory in MB.  
[linearMemoryGrowthStep](PlayerSettings.WebGL-linearMemoryGrowthStep.html)|
Heap memory growth step in MB.  
[linkerTarget](PlayerSettings.WebGL-linkerTarget.html)| Allows you to specify
the web build format that is used when you build your project.  
[maximumMemorySize](PlayerSettings.WebGL-maximumMemorySize.html)| Maximum size
of the WASM heap memory in MB.  
[memoryGeometricGrowthCap](PlayerSettings.WebGL-
memoryGeometricGrowthCap.html)| Upper limit for heap growth step in MB.  
[memoryGrowthMode](PlayerSettings.WebGL-memoryGrowthMode.html)| The growth
mode for WASM heap memory.  
[memorySize](PlayerSettings.WebGL-memorySize.html)| Memory size for WebGL
builds in Megabyte.  
[nameFilesAsHashes](PlayerSettings.WebGL-nameFilesAsHashes.html)| Enables
using MD5 hash of the uncompressed file contents as a filename for each file
in the build.  
[powerPreference](PlayerSettings.WebGL-powerPreference.html)| The power
preference hint to provide to the WebGL context to help decide which GPU to
use in multi-gpu systems. Note that this is just a hint, and some WebGL
implementations may choose to ignore it.  
[showDiagnostics](PlayerSettings.WebGL-showDiagnostics.html)| Displays a
diagnostics overlay on the Unity application page.  
[template](PlayerSettings.WebGL-template.html)| Path to the WebGL template
asset.  
[threadsSupport](PlayerSettings.WebGL-threadsSupport.html)| Multithreading
support in WebGL.  
[wasm2023](PlayerSettings.WebGL-wasm2023.html)| If enabled, generated
WebAssembly code will target "WebAssembly 2023", a Unity-coined name for a
selection of newer WebAssembly language features. These features include:
sign-extension opcodes, non-trapping fp-to-int instructions, bulk memory, JS
BigInt integration, WebAssembly.Table, native WebAssembly exceptions and SIMD.
Requires Chrome ≥ 91 (May 2021), Firefox ≥ 89 (June 2021) or Safari ≥ 16.4
(March 2023). If disabled, targets the original WebAssembly "MVP" feature set.  
[wasmArithmeticExceptions](PlayerSettings.WebGL-
wasmArithmeticExceptions.html)| The trapping mode for WebAssembly code.  
[webAssemblyBigInt](PlayerSettings.WebGL-webAssemblyBigInt.html)| If enabled,
generated WebAssembly code will rely on the BigInt ABI for function signatures
containing 64-bit variables. Enable this to achieve faster build times and
slightly smaller code size. The Wasm BigInt feature requires at least Chrome
85 (Aug 25, 2020), Firefox 78 (Jun 30, 2020), Safari 14.5 (Apr 26, 2021), or
newer. Disable this option to target older browsers that do not support the
Wasm BigInt feature. It is recommended to enable this option for new projects
and if you prefer fast build iteration times, and to disable it if targeting
backward compatibility with older browsers is important.  
[webAssemblyTable](PlayerSettings.WebGL-webAssemblyTable.html)| If enabled,
targets the WebAssembly.Table language feature, which results in faster JS-
Wasm interop and faster build times. WebAssembly.Table is not backwards
compatible with the older dynCalls interop model. If disabled, Unity targets
the old deprecated Emscripten -sDYNCALLS flag for backwards compatibility with
older Unity Web platform JS plugin code. It is recommended to enable this
option for new projects that do not utilize any older incompatible JavaScript
plugins, and when fast you prefer build iteration times, and to disable it if
utilizing .jslib files that rely on the older dynCall() mechanism.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

