[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-display-types.html)
  * [中文](/cn/current/Manual/writing-shader-display-types.html)
  * [日本語](/ja/current/Manual/writing-shader-display-types.html)
  * [한국어](/kr/current/Manual/writing-shader-display-types.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-display-types.html)
  * [中文](/cn/current/Manual/writing-shader-display-types.html)
  * [日本語](/ja/current/Manual/writing-shader-display-types.html)
  * [한국어](/kr/current/Manual/writing-shader-display-types.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Adding material properties to shaders](writing-shader-change-properties.html)
  * Control material properties in the Inspector window

[](writing-shader-use-material-properties.html)

Set shader variables with material property values

[](SL-MultipleProgramVariants.html)

Changing how shaders work via branching and keywords

# Control material properties in the Inspector window

In the Unity Editor, you can control how material properties appear in the
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window. The easiest way to do this
is using a
[MaterialPropertyDrawer](../ScriptReference/MaterialPropertyDrawer.html).

For more complex needs, you can use the
[MaterialEditor](../ScriptReference/MaterialEditor.html),
[MaterialProperty](../ScriptReference/MaterialProperty.html), and
[ShaderGUI](../ScriptReference/ShaderGUI.html) classes.

## Use a custom editor

Use custom editors to display data types that Unity can’t display using its
default material Inspector, or to define custom controls or data validation.

In **ShaderLab** Unity’s language for defining the structure of Shader
objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab), you can assign a custom editor for
all **render pipelines** A series of operations that take the contents of a
Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline). To do this, you can place a
`CustomEditor` block inside a `Shader` block. You can also assign different
custom editors for render pipelines based on the Scriptable Render Pipeline by
placing a `CustomEditorForRenderPipeline` block inside a `Shader` block. If
your code contains both a `CustomEditor` and `CustomEditorForRenderPipeline`
block, the render pipeline specific one overrides the `CustomEditor` one.

### Create a custom editor class for a shader asset

To define a custom editor for **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) assets that represent a given **Shader
object** An instance of the Shader class, a Shader object is container for
shader programs and GPU instructions, and information that tells Unity how to
use them. Use them with materials to determine the appearance of your scene.
[More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject), you create a script that
inherits from the [ShaderGUI](../ScriptReference/ShaderGUI.html) class. Place
your script in a folder named _Editor_ , in your _Assets_ folder.

The script should follow this format:

    
    
    using UnityEditor;
    
    public class ExampleShaderGUI : ShaderGUI 
    {
        public override void OnGUI (MaterialEditor materialEditor, MaterialProperty[] properties)
        {
            // Custom code that controls the appearance of the Inspector goes here
    
            base.OnGUI (materialEditor, properties);
        }
    }
    

### Enable the default custom editor

This example code demonstrates the syntax for specifying a default custom
editor for a shader asset using the `CustomEditor` block, and then specifying
two additional custom editors for specific Render Pipeline Assets using the
`CustomEditorForRenderPipeline` block.

    
    
    Shader "Examples/UsesCustomEditor"
    {
        // The Unity Editor uses the class ExampleCustomEditor to configure the Inspector for this shader asset
        CustomEditor "ExampleShaderGUI"
        CustomEditorForRenderPipeline "ExampleRenderPipelineShaderGUI" "ExampleRenderPipelineAsset"
        CustomEditorForRenderPipeline "OtherExampleRenderPipelineShaderGUI" "OtherExampleRenderPipelineAsset"
    
        SubShader
        {
            // Code that defines the SubShader goes here.
    
            Pass
            {                
                  // Code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [Custom Editor block in ShaderLab reference](SL-CustomEditor.html)

[](writing-shader-use-material-properties.html)

Set shader variables with material property values

[](SL-MultipleProgramVariants.html)

Changing how shaders work via branching and keywords

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

