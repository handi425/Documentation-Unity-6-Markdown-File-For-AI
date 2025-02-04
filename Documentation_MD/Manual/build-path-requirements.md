[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/build-path-requirements.html)
  * [中文](/cn/current/Manual/build-path-requirements.html)
  * [日本語](/ja/current/Manual/build-path-requirements.html)
  * [한국어](/kr/current/Manual/build-path-requirements.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/build-path-requirements.html)
  * [中文](/cn/current/Manual/build-path-requirements.html)
  * [日本語](/ja/current/Manual/build-path-requirements.html)
  * [한국어](/kr/current/Manual/build-path-requirements.html)

  * [Platform development ](PlatformSpecific.html)
  * [Cross-platform features and considerations](cross-platform-features.html)
  * Build path requirements for target platforms

[](XcodeFrameDebuggerIntegration.html)

Xcode frame debugger Unity integration

[](GraphicsAPIs.html)

Graphics API support

# Build path requirements for target platforms

When you’re building Players for target platforms using [command-line
arguments](CommandLineArguments.html) or C# APIs, such as
[BuildPipeline.BuildPlayer](../ScriptReference/BuildPipeline.BuildPlayer.html),
you must specify the path for the build location. For certain platforms, this
path must also include the build file extension specific to the platform.

The following table lists such platforms that require you to include build
file extensions when building Players using command-line arguments or C# APIs.

**Platform** | **Build file extension**  
---|---  
**Android** | • **Android Package** : `.apk`  
• **Android App Bundle** :`.aab`  
  
**Note** : The file extension isn’t required for the following conditions:  
• When building a Gradle project using **Export Project** build setting  
• When building the Android App Bundle using **Export for App Bundle** build
setting.  
  
Instead, specify the folder name for the exported Gradle project or Android
App Bundle in the build path.  
**Windows (Standalone and Server)** |  `.exe`  
  
**Note** : The file extension isn’t required when generating a Visual Studio
Solution using the **Create Visual Studio Solution** build setting. Instead,
specify the folder name for the generated Visual Studio Solution in the build
path.  
**macOS (Standalone)** |  `.app`  
  
**Note** : The file extension isn’t required when generating an Xcode project
using the **Create Xcode Project** build setting. Instead, specify the folder
name for the generated Xcode project in the build path.  
**Linux (Standalone and Server)** | `.x86_64`  
  
## Additional resources

  * [BuildPipeline.BuildPlayer](../ScriptReference/BuildPipeline.BuildPlayer.html)
  * [Command-line arguments](CommandLineArguments.html)

[](XcodeFrameDebuggerIntegration.html)

Xcode frame debugger Unity integration

[](GraphicsAPIs.html)

Graphics API support

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

