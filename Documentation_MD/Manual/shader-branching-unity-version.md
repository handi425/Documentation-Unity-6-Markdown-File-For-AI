[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-branching-unity-version.html)
  * [中文](/cn/current/Manual/shader-branching-unity-version.html)
  * [日本語](/ja/current/Manual/shader-branching-unity-version.html)
  * [한국어](/kr/current/Manual/shader-branching-unity-version.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-branching-unity-version.html)
  * [中文](/cn/current/Manual/shader-branching-unity-version.html)
  * [日本語](/ja/current/Manual/shader-branching-unity-version.html)
  * [한국어](/kr/current/Manual/shader-branching-unity-version.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Branching in shaders](shader-branching.html)
  * [Branch in a shader via built-in macros](shader-branching-built-in-macros.html)
  * Branch based on Unity version

[](shader-branching-platform.html)

Branch based on platform features

[](shader-branching-pass.html)

Branch based on shader pass or shader stage

# Branch based on Unity version

`UNITY_VERSION` contains the numeric value of the Unity version.

This can be used for version comparisons if you need to write shaders that use
different built-in shader functionality. For example, use `#if UNITY_VERSION
>= 202200` if you want the preprocessor check to pass only on Unity versions
2022 or later.

## Unity 2023 or earlier

Use the format `YYYYMP`, where:

  * `YYYY` is the major version.
  * `M` is the minor version.
  * `P` is the patch version.

For example, for Unity 2022.3.0, use `202230`.

You can use only values up to 9 for the minor and patch versions. This means
you can’t check for a Unity version with a minor version larger than 9 or a
patch version larger than 9.

## Unity 6 Preview

Use the format `6000PPPP`, where:

  * `6000` is Unity 6.
  * `PPPP` is the patch version with leading zeroes, for example `1234` for Unity 6000.0.1234.

For example, for Unity 6000.0.2, use `60000002`.

[](shader-branching-platform.html)

Branch based on platform features

[](shader-branching-pass.html)

Branch based on shader pass or shader stage

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

