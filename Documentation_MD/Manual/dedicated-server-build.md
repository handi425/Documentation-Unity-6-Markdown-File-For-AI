[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dedicated-server-build.html)
  * [中文](/cn/current/Manual/dedicated-server-build.html)
  * [日本語](/ja/current/Manual/dedicated-server-build.html)
  * [한국어](/kr/current/Manual/dedicated-server-build.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dedicated-server-build.html)
  * [中文](/cn/current/Manual/dedicated-server-build.html)
  * [日本語](/ja/current/Manual/dedicated-server-build.html)
  * [한국어](/kr/current/Manual/dedicated-server-build.html)

  * [Platform development ](PlatformSpecific.html)
  * [Dedicated Server](dedicated-server.html)
  * Build your application for Dedicated Server 

[](dedicated-server-optimizations.html)

Dedicated Server optimizations

[](dedicated-server-assetbundles.html)

Dedicated Server AssetBundles

# Build your application for Dedicated Server

You can create a Dedicated Server build in either of the following ways:

  * Unity Editor
  * Scripting
  * Command line

## Unity Editor

To create a Dedicated Server build in the Unity Editor, use the following
steps:

  1. Open the [Build Profiles](BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile) window from **File** > **Build
Profiles**.

  2. Select **Add Build Profile** to open the **Platform Browser** window.
  3. Select the type of server to build from the list of available platforms. For example, select **Linux Server** to build a Linux server.
  4. If the server type isn’t available, select **Install with Unity Hub** and follow the installation instructions. For information on how to install modules, refer to [Add modules](https://docs.unity3d.com/hub/manual/AddModules.html).
  5. Select **Switch Profile** to set the new build profile as the active profile.
  6. Click **Build**.

**Tip** : You can further configure the Dedicated Server build in the [Player
settings](dedicated-server-player-settings.html)Settings that let you set
various player-specific options for the final game built by Unity. [More
info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings).

## Scripting

To create a Dedicated Server build using a script, set
`buildPlayerOptions.subtarget` to `(int)StandaloneBuildSubtarget.Server`.

    
    
    buildPlayerOptions.target = BuildTarget.StandaloneWindows;
    // SubTarget expects an integer.
    buildPlayerOptions.subtarget = (int)StandaloneBuildSubtarget.Server;
    

## Command line

To create a Dedicated Server build through the command line, use the
`-standaloneBuildSubtarget Server` [argument](CommandLineArguments.html).

    
    
    -buildTarget Linux64 -standaloneBuildSubtarget Server
    

## Code sign macOS Dedicated Server builds

Dedicated Server builds that aren’t code signed might display security
warnings when deployed on macOS systems. To avoid such warnings, make sure you
code sign the build before distribution. For more information, refer to the
documentation on [Code sign and notarize your macOS application](macos-
building-notarization.html).

## Additional resources

  * [macOS Build Settings reference](macosbuildsettings.html)
  * [Windows Build Settings reference](WindowsStandaloneBinaries.html)
  * [Linux Build Settings reference](Buildsettings-linux.html)
  * [Creating and Using Scripts](creating-scripts.html)

[](dedicated-server-optimizations.html)

Dedicated Server optimizations

[](dedicated-server-assetbundles.html)

Dedicated Server AssetBundles

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

