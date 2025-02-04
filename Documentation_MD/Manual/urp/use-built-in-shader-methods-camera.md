[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/use-built-in-shader-methods-camera.html)
  * [中文](/cn/current/Manual/urp/use-built-in-shader-methods-camera.html)
  * [日本語](/ja/current/Manual/urp/use-built-in-shader-methods-camera.html)
  * [한국어](/kr/current/Manual/urp/use-built-in-shader-methods-camera.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/use-built-in-shader-methods-camera.html)
  * [中文](/cn/current/Manual/urp/use-built-in-shader-methods-camera.html)
  * [日本語](/ja/current/Manual/urp/use-built-in-shader-methods-camera.html)
  * [한국어](/kr/current/Manual/urp/use-built-in-shader-methods-camera.html)

  * [Materials and shaders](../materials-and-shaders.html)
  * [Shaders](../Shaders.html)
  * [Shaders in URP](../urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](../urp/writing-custom-shaders-urp.html)
  * [Shader methods in URP](../urp/use-built-in-shader-methods.html)
  * Use the camera in a custom URP shader

[](../urp/use-built-in-shader-methods-transformations.html)

Transform positions in a custom URP shader

[](../urp/use-built-in-shader-methods-lighting.html)

Use lighting in a custom URP shader

# Use the camera in a custom URP shader

To use the **camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) in a custom Universal **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) **shader** A program
that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader), follow these steps:

  1. Add `#include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"` inside the `HLSLPROGRAM` in your shader file. The `Core.hlsl` file imports the `ShaderVariablesFunction.hlsl` file.
  2. Use one of the following methods from the `ShaderVariablesFunction.hlsl` file.

**Method** | **Syntax** | **Description**  
---|---|---  
`GetCameraPositionWS` | `float3 GetCameraPositionWS()` | Returns the world space position of the camera.  
`GetScaledScreenParams` | `float4 GetScaledScreenParams()` | Returns the width and height of the screen in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel).  
`GetViewForwardDir` | `float3 GetViewForwardDir()` | Returns the forward direction of the view in world space.  
`IsPerspectiveProjection` | `bool IsPerspectiveProjection()` | Returns `true` if the camera projection is set to perspective.  
`LinearDepthToEyeDepth` | `half LinearDepthToEyeDepth(half linearDepth)` | Converts a linear **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](../class-RenderTexture.html)  
See in [Glossary](../Glossary.html#depthbuffer) value to view depth. Refer to
[Cameras and depth textures](https://docs.unity3d.com/Manual/SL-
CameraDepthTexture.html) for more information.  
`TransformScreenUV` | `void TransformScreenUV(inout float2 screenSpaceUV)` | Flips the y coordinate of the screen space position, if Unity uses an upside-down coordinate space. You can also input both a `uv`, and the screen height as a `float`, so the method outputs the position scaled to the screen size in pixels.  
  
## Example

The following URP shader draws object surfaces with colors that represent the
direction from the surface to the camera.

    
    
    Shader "Custom/DirectionToCamera"
    {
        SubShader
        {
            Tags { "RenderType" = "Opaque" "RenderPipeline" = "UniversalPipeline" }
    
            Pass
            {
                HLSLPROGRAM
    
                #pragma vertex vert
                #pragma fragment frag
    
                #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"
    
                struct Attributes
                {
                    float4 positionOS : POSITION;
                    float2 uv: TEXCOORD0;
                };
    
                struct Varyings
                {
                    float4 positionCS  : SV_POSITION;
                    float2 uv: TEXCOORD0;
                    float3 viewDirection : TEXCOORD2;
                };
    
                Varyings vert(Attributes IN)
                {
                    Varyings OUT;
    
                    // Get the positions of the vertex in different coordinate spaces
                    VertexPositionInputs positions = GetVertexPositionInputs(IN.positionOS);
                    OUT.positionCS = positions.positionCS;
    
                    // Get the direction from the vertex to the camera, in world space
                    OUT.viewDirection = GetCameraPositionWS() - positions.positionWS.xyz;
    
                    return OUT;
                }
    
                half4 frag(Varyings IN) : SV_Target
                {
                    // Set the fragment color to the direction vector
                    return float4(IN.viewDirection, 1);
                }
                ENDHLSL
            }
        }
    }
    

## Additional resources

  * [Cameras in URP](cameras/camera-differences-in-urp.html)
  * [Writing custom shaders](writing-custom-shaders-urp.html)
  * [Upgrade custom shaders for URP compatibility](urp-shaders/birp-urp-custom-shader-upgrade-guide.html)
  * [HLSL in Unity](https://docs.unity3d.com/Manual/SL-ShaderPrograms.html)

[](../urp/use-built-in-shader-methods-transformations.html)

Transform positions in a custom URP shader

[](../urp/use-built-in-shader-methods-lighting.html)

Use lighting in a custom URP shader

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

