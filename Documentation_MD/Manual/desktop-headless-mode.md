[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/desktop-headless-mode.html)
  * [中文](/cn/current/Manual/desktop-headless-mode.html)
  * [日本語](/ja/current/Manual/desktop-headless-mode.html)
  * [한국어](/kr/current/Manual/desktop-headless-mode.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/desktop-headless-mode.html)
  * [中文](/cn/current/Manual/desktop-headless-mode.html)
  * [日本語](/ja/current/Manual/desktop-headless-mode.html)
  * [한국어](/kr/current/Manual/desktop-headless-mode.html)

  * [Platform development ](PlatformSpecific.html)
  * [Dedicated Server](dedicated-server.html)
  * Desktop headless mode

[](dedicated-server-assetbundles.html)

Dedicated Server AssetBundles

[](embedded-systems.html)

Embedded systems

# Desktop headless mode

The Dedicated Server build target is similar to the desktop headless mode. The
only difference is that the Dedicated Server build target is optimized to
increase memory and CPU performance when running as a networked application.

Desktop headless mode allows you to run applications in batchmode on any
desktop platform without initializing the graphics device. You can run desktop
headless mode by passing the `-batchmode` and `-nographics` command line
arguments when executing the Player. You can’t select headless mode from the
Unity Editor Build Settings, but you can add the `-batchmode` and
`-nographics` command line arguments to effectively create a headless build.

Desktop headless mode doesn’t perform any optimizations for running a build as
a dedicated server. Although the Dedicated Server build option performs
additional optimizations, you might still want to use desktop headless mode
for other purposes, such as automated testing on CI/CD platforms.

[](dedicated-server-assetbundles.html)

Dedicated Server AssetBundles

[](embedded-systems.html)

Embedded systems

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

