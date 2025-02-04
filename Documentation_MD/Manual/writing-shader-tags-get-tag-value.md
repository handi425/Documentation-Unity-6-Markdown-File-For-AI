[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-tags-get-tag-value.html)
  * [中文](/cn/current/Manual/writing-shader-tags-get-tag-value.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-get-tag-value.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-get-tag-value.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-tags-get-tag-value.html)
  * [中文](/cn/current/Manual/writing-shader-tags-get-tag-value.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-get-tag-value.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-get-tag-value.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Configure when and if Unity uses a shader](writing-shader-tags.html)
  * Get tag values in a script

[](writing-shader-tags-disable-dynamic-batching.html)

Disable dynamic batching of a shader

[](writing-shader-tags-require-package-troubleshooting.html)

Troubleshooting package requirement definitions

# Get tag values in a script

## Using SubShader tags with C# code

You can read SubShader tags from a C# script using the
[Material.GetTag](../ScriptReference/Material.GetTag.html) API, like this:

    
    
    using UnityEngine;
    
    public class Example : MonoBehaviour
    {
        // Attach this to a gameObject that has a Renderer component
        string tagName = "ExampleTagName";
    
        void Start()
        {
            Renderer myRenderer = GetComponent<Renderer>();
            string tagValue = myRenderer.material.GetTag(ExampleTagName, true, "Tag not found");
            Debug.Log(tagValue);
        }
    }
    

### Queue tag

You can use [Shader.renderQueue](../ScriptReference/Shader-renderQueue.html)
to read the Queue tag value of a **Shader** A program that runs on the GPU.
[More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) object’s active SubShader.

By default, Unity renders geometry in the render queue specified in the
[Queue] tag. You can override this value on a per-material basis. In the Unity
Editor, you can do this in the [material Inspector](class-Material.html) by
setting the **Render Queue** property. In a C# script, you can do this by
setting the value of [Material.renderQueue](../ScriptReference/Material-
renderQueue.html) using the
[Rendering.RenderQueue](../ScriptReference/Rendering.RenderQueue.html) enum.

## Using Pass tags with C# code

To access the value of a Pass tag from C# **scripts** A piece of code that
allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), you can use the
[Shader.FindPassTagValue](../ScriptReference/Shader.FindPassTagValue.html)
API. This works for Unity’s predefined Pass tags, and for custom Pass tags
that you have created.

### Using the LightMode tag with C# scripts

[Material.SetShaderPassEnabled](../ScriptReference/Material.SetShaderPassEnabled.html)
and [ShaderTagId](../ScriptReference/Rendering.ShaderTagId.html) use the value
of the `LightMode` tag to determine how Unity handles a given Pass.

In the Scriptable **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), you can create custom values
for the `LightMode` tag. You can then use these custom values to determine
which Passes to draw during a given call to
[ScriptableRenderContext.DrawRenderers](../ScriptReference/Rendering.ScriptableRenderContext.DrawRenderers.html),
by configuring a
[DrawingSettings](../ScriptReference/Rendering.DrawingSettings.html) struct.
For more information and a code example, see [Creating a simple render loop in
a custom Scriptable Render
Pipeline](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.core@17.0/manual/index.html).

## Additional resources

  * [SubShader tags in ShaderLab reference](SL-SubShaderTags.html)
  * [Pass tags in ShaderLab reference](SL-PassTags.html)

[](writing-shader-tags-disable-dynamic-batching.html)

Disable dynamic batching of a shader

[](writing-shader-tags-require-package-troubleshooting.html)

Troubleshooting package requirement definitions

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

