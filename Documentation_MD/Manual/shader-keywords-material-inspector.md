[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-keywords-material-inspector.html)
  * [中文](/cn/current/Manual/shader-keywords-material-inspector.html)
  * [日本語](/ja/current/Manual/shader-keywords-material-inspector.html)
  * [한국어](/kr/current/Manual/shader-keywords-material-inspector.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-keywords-material-inspector.html)
  * [中文](/cn/current/Manual/shader-keywords-material-inspector.html)
  * [日本語](/ja/current/Manual/shader-keywords-material-inspector.html)
  * [한국어](/kr/current/Manual/shader-keywords-material-inspector.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Shader keywords](shader-keywords-landing.html)
  * Add shader keywords to the Inspector window

[](SL-MultipleProgramVariants-make-conditionals.html)

Make shader behavior conditional on keywords

[](shader-keywords-scripts.html)

Toggle and check shader keywords in a script

# Add shader keywords to the Inspector window

In the Unity Editor, when you view a material in the material **Inspector** A
Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), you can enable and disable its
local **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) keywords. This is useful for two
reasons:

  * It allows artists to easily set different keyword values for different materials, without needing to use code.
  * When you enable a keyword using the `[KeywordEnum]` MaterialPropertyDrawer, Unity automatically disables the other keywords in a set. This ensures that exactly one keyword from a set is enabled at any time.

As with any shader settings or data, shader keywords are only available in the
material Inspector when they are declared as [material properties](SL-
Properties.html) in the shader source file.

For shaders created in Shader Graph, keywords are material properties by
default. This means that these settings are automatically available in the
material Inspector. To change this, open the
[Blackboard](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest?subfolder=/manual/Blackboard.html),
and change the **Exposed** property.

For hand-coded shaders, you must ensure that your **ShaderLab** Unity’s
language for defining the structure of Shader objects. [More info](SL-
Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) code defines a [material
property](SL-Properties.html) that represents the keyword set. The material
property must have a type of `Float`, and must use the `[Toggle]`,
`[ToggleOff]`, or `[KeywordEnum]`
[MaterialPropertyDrawer](../ScriptReference/MaterialPropertyDrawer.html)
attribute to expose it correctly to the Inspector.

The following example adds a toggle called **Make Red** , which enables and
disables the keyword `_RED_ON`.

    
    
    Shader "Unlit/ToggleRed"
    {
        Properties
        {
            [Toggle] _RED ("Make red", Float) = 0
        }
        SubShader
        {
            Tags { "RenderType"="Opaque" }
    
            Pass
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
    
                // Add the keyword RED_ON, for when the toggle is on
                // Unity automatically adds a keyword for when the toggle is off 
                #pragma shader_feature _RED_ON
    
                #include "UnityCG.cginc"
    
                struct appdata
                {
                    float4 vertex : POSITION;
                };
    
                struct v2f
                {
                    float4 vertex : SV_POSITION;
                };
    
                v2f vert (appdata v)
                {
                    v2f o;
                    o.vertex = UnityObjectToClipPos(v.vertex);
                    return o;
                }
    
                fixed4 frag (v2f i) : SV_Target
                {
                    // Return red if the toggle is on
                    #if _RED_ON
                        return fixed4(1, 0, 0, 1);
                    #else
                        return fixed4(0, 0, 0, 1);
                    #endif
                }
                ENDCG
            }
        }
    }
    

For more information and examples, see the documentation for the
[MaterialPropertyDrawer](../ScriptReference/MaterialPropertyDrawer.html) API.

## Additional resources

  * [Adding material properties to shaders](writing-shader-change-properties.html)
  * [Properties block reference in ShaderLab](SL-Properties.html)

[](SL-MultipleProgramVariants-make-conditionals.html)

Make shader behavior conditional on keywords

[](shader-keywords-scripts.html)

Toggle and check shader keywords in a script

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

