[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dedicated-server-introduction.html)
  * [中文](/cn/current/Manual/dedicated-server-introduction.html)
  * [日本語](/ja/current/Manual/dedicated-server-introduction.html)
  * [한국어](/kr/current/Manual/dedicated-server-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dedicated-server-introduction.html)
  * [中文](/cn/current/Manual/dedicated-server-introduction.html)
  * [日本語](/ja/current/Manual/dedicated-server-introduction.html)
  * [한국어](/kr/current/Manual/dedicated-server-introduction.html)

  * [Platform development ](PlatformSpecific.html)
  * [Dedicated Server](dedicated-server.html)
  * Introduction to Dedicated Server

[](dedicated-server.html)

Dedicated Server

[](dedicated-server-get-started.html)

Get started with Dedicated Server

# Introduction to Dedicated Server

Dedicated Server refers to a computer that’s optimized to run server
applications.

The Dedicated Server [build target](../ScriptReference/BuildTarget.html) is a
sub-target of the three Desktop Platforms (Linux, macOS, and Windows) that’s
optimized for running as a dedicated server. Using Dedicated Server build
target, you can cut back on your server builds’ CPU, memory, and disk space
requirements.

Server builds often contain unnecessary assets and compiled code for headless
server processes. The build data might include artifacts such as audio files,
textures, meshes, and **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). In a multiplayer context, rendering
and asset management processes occur unnecessarily when building and executing
server runtimes.

The goal of the Dedicated Server build target is to reduce the resource demand
of server builds, including the disk size, the size in memory, and the CPU
usage. Most of the optimizations take place through [stripping code](managed-
code-stripping.html) and assets that aren’t necessary for a server build.

## Additional resources

  * [Desktop headless mode](desktop-headless-mode.html)

[](dedicated-server.html)

Dedicated Server

[](dedicated-server-get-started.html)

Get started with Dedicated Server

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

