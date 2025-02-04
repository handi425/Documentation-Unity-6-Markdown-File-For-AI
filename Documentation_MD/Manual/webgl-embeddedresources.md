[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/webgl-embeddedresources.html)
  * [中文](/cn/current/Manual/webgl-embeddedresources.html)
  * [日本語](/ja/current/Manual/webgl-embeddedresources.html)
  * [한국어](/kr/current/Manual/webgl-embeddedresources.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/webgl-embeddedresources.html)
  * [中文](/cn/current/Manual/webgl-embeddedresources.html)
  * [日本語](/ja/current/Manual/webgl-embeddedresources.html)
  * [한국어](/kr/current/Manual/webgl-embeddedresources.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * Embedded resources in Web

[](webgl-texture-compression.html)

Texture compression in Web

[](webgl-input.html)

Input in Web

# Embedded resources in Web

.NET assemblies can contain embedded resources. An embedded resource is a
collection of binary data that’s part of the .NET assembly. You can access
this binary data in code via a file-like API.

By default, Web builds don’t include embedded resources. This helps to keep
the size of the final binary lower, because embedded resources can be rather
large. However, some user code and .NET class library APIs depend on the
presence of embedded resources to work properly. For example, string
comparisons that use the `StringComparison.InvariantCultureIgnoreCase` value
use embedded resources when comparing non-ASCII characters.

You can use the following script in the Unity Editor to enable embedded
resources for a Web build:

    
    
    using UnityEditor;
    
    public class WebGLEditorScript
    {
        [MenuItem("WebGL/Enable Embedded Resources")]
        public static void EnableEmbeddedResources()
        {
            PlayerSettings.WebGL.useEmbeddedResources = true;
        }
    }
    

When this Player setting is enabled, the Web build includes any embedded
resources in any .NET assemblies the Project uses.

[](webgl-texture-compression.html)

Texture compression in Web

[](webgl-input.html)

Input in Web

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

