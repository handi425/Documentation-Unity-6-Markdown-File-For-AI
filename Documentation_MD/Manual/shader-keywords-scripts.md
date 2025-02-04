[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-keywords-scripts.html)
  * [中文](/cn/current/Manual/shader-keywords-scripts.html)
  * [日本語](/ja/current/Manual/shader-keywords-scripts.html)
  * [한국어](/kr/current/Manual/shader-keywords-scripts.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-keywords-scripts.html)
  * [中文](/cn/current/Manual/shader-keywords-scripts.html)
  * [日本語](/ja/current/Manual/shader-keywords-scripts.html)
  * [한국어](/kr/current/Manual/shader-keywords-scripts.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Shader keywords](shader-keywords-landing.html)
  * Toggle and check shader keywords in a script

[](shader-keywords-material-inspector.html)

Add shader keywords to the Inspector window

[](shaders-keywords-built-in.html)

Built-in keywords

# Toggle and check shader keywords in a script

## Check if a keyword is enabled or disabled

When a global and local **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) keyword with the same name have
different states, Unity uses the `isOverridable` property of a `LocalKeyword`
to determine whether the keyword is enabled or disabled for an individual
material or compute shader. `isOverridable` is true if the keyword was
declared with global scope, and `false` if it was declared with local scope.

  * When `isOverridable` is `true`: If a global keyword with the same name exists and is enabled, Unity uses the state of the global keyword. Otherwise, Unity uses the state of the local keyword.
  * When `isOverridable` is `false`: Unity always uses the state of the local keyword.

Therefore, to understand whether a shader keyword is enabled or disabled for
an individual material or compute shader, you must examine the state of the
`isOverridable` property and the global and/or local keyword state.

This example demonstrates how to check whether Unity considers a keyword
enabled or disabled for a material:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    
    public class KeywordExample : MonoBehaviour
    {
        public Material material;
    
        void Start()
        {
            CheckShaderKeywordState();
        }
    
        void CheckShaderKeywordState()
        {
            // Get the instance of the Shader class that the material uses
            var shader = material.shader;
    
            // Get all the local keywords that affect the Shader
            var keywordSpace = shader.keywordSpace;
    
            // Iterate over the local keywords
            foreach (var localKeyword in keywordSpace.keywords)
            {
                // If the local keyword is overridable (i.e., it was declared with a global scope),
                // and a global keyword with the same name exists and is enabled,
                // then Unity uses the global keyword state
                if (localKeyword.isOverridable && Shader.IsKeywordEnabled(localKeyword.name))
                {
                    Debug.Log("Local keyword with name of " + localKeyword.name + " is overridden by a global keyword, and is enabled");
                }
                // Otherwise, Unity uses the local keyword state
                else
                {
                    var state = material.IsKeywordEnabled(localKeyword) ? "enabled" : "disabled";
                    Debug.Log("Local keyword with name of " + localKeyword.name + " is " + state);
                }            
            }
        }
    }
    
    

## Enabling and disabling shader keywords

To check whether a local keyword is enabled for a graphics shader, use
[Material.IsKeywordEnabled](../ScriptReference/Material.IsKeywordEnabled.html)
or [Material.EnableKeyword](../ScriptReference/Material.EnableKeyword.html).
For a compute shader, use
[ComputeShader.IsKeywordEnabled](../ScriptReference/ComputeShader.IsKeywordEnabled.html),
or
[ComputeShader.EnableKeyword](../ScriptReference/ComputeShader.EnableKeyword.html).

To check whether a global keyword is enabled, use
[Shader.IsKeywordEnabled](../ScriptReference/Shader.IsKeywordEnabled.html) or
[Shader.EnableKeyword](../ScriptReference/Shader.EnableKeyword.html) or
[ComputeShader.enabledKeywords](../ScriptReference/ComputeShader-
enabledKeywords.html).

To enable or disable a local shader keyword for a graphics shader, use
[Material.SetKeyword](../ScriptReference/Material.SetKeyword.html),
[Material.EnableKeyword](../ScriptReference/Material.EnableKeyword.html), or
[Material.DisableKeyword](../ScriptReference/Material.DisableKeyword.html).
For a compute shader, use
[ComputeShader.SetKeyword](../ScriptReference/ComputeShader.SetKeyword.html),
[ComputeShader.EnableKeyword](../ScriptReference/ComputeShader.EnableKeyword.html),
or
[ComputeShader.DisableKeyword](../ScriptReference/ComputeShader.DisableKeyword.html).

To enable or disable a global shader keyword, use
[Shader.SetKeyword](../ScriptReference/Shader.SetKeyword.html),
[ComputeShader.EnableKeyword](../ScriptReference/Shader.EnableKeyword.html),
or
[ComputeShader.DisableKeyword](../ScriptReference/Shader.DisableKeyword.html).

To enable or disable a local or global keyword with a Command Buffer, use
[CommandBuffer.EnableKeyword](../ScriptReference/Rendering.CommandBuffer.EnableKeyword.html),
or
[CommandBuffer.DisableKeyword](../ScriptReference/Rendering.CommandBuffer.DisableKeyword.html)
.

**Note:** When you enable or disable keywords that work with shader variants,
Unity uses different shader variants. Changing shader variants at runtime can
impact performance. If a change in keywords requires a variant to be used for
the first time, it can lead to hitches while the graphics driver prepares the
shader program. This can be a particular problem for large or complex shaders,
or if a global keyword state change affects multiple shaders. To avoid this,
if you use keywords with shader variants, ensure that you consider keyword
variants in your shader loading and prewarming strategy. For more information,
see [Shader loading](shader-loading.html).

## Check if a keyword was declared for dynamic branching

In Unity, you can use shader keywords with shader variants, or you can use
them with dynamic branching. You decide when you declare the keywords.

The [isDynamic](../ScriptReference/Rendering.LocalKeyword-isDynamic.html)
property of a `LocalKeyword` indicates whether the keyword was declared for
use with dynamic branching in the shader source file. It is `true` if the
keyword was declared for use with dynamic branching, and `false` if it was
declared for use with shader variants.

## Additional resources

  * [Shader keyword scope fundamentals](shader-keywords-scope-fundamentals.html)

[](shader-keywords-material-inspector.html)

Add shader keywords to the Inspector window

[](shaders-keywords-built-in.html)

Built-in keywords

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

