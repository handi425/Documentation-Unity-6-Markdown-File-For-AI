[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-ShaderReplacement.html)
  * [中文](/cn/current/Manual/SL-ShaderReplacement.html)
  * [日本語](/ja/current/Manual/SL-ShaderReplacement.html)
  * [한국어](/kr/current/Manual/SL-ShaderReplacement.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-ShaderReplacement.html)
  * [中文](/cn/current/Manual/SL-ShaderReplacement.html)
  * [日本語](/ja/current/Manual/SL-ShaderReplacement.html)
  * [한국어](/kr/current/Manual/SL-ShaderReplacement.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * Replace shaders at runtime in the Built-In Render Pipeline

[](Shader-Autodesk-Interactive.html)

Autodesk Interactive shader in the Built-In Render Pipeline

[](writing-shaders-birp.html)

Writing custom shaders in the Built-In Render Pipeline

# Replace shaders at runtime in the Built-In Render Pipeline

In the Built-in **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), you can tell a **Camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) to change the shader that it uses to
render certain geometry at runtime. You might do this to achieve a visual
effect such as edge detection.

Shader replacement is done from **scripts** A piece of code that allows you to
create your own Components, trigger game events, modify Component properties
over time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts) with either the
[Camera.RenderWithShader](../ScriptReference/Camera.RenderWithShader.html) or
[Camera.SetReplacementShader](../ScriptReference/Camera.SetReplacementShader.html)
function. Both functions take a **shader** A program that runs on the GPU.
[More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) and a **replacementTag**.

It works like this: the camera renders the **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) as it normally would. The objects still
use their materials, but the shader they use changes:

  * If **replacementTag** is empty (must be an empty string not null), then all objects in the scene are rendered with the given replacement shader.
  * If **replacementTag** is not empty, then for each object that would be rendered: 
    * The real object’s shader is queried for the [tag value](SL-SubShaderTags.html).
    * If it does not have that tag, object is **not rendered**.
    * A [subshader](SL-SubShader.html) is found in the replacement shader that has a given tag with the found value. If no such subshader is found, object is **not rendered**.
    * Now that subshader is used to render the object.

So if all shaders would have, for example, a “RenderType” tag with values like
“Opaque”, “Transparent”, “Background”, “Overlay”, you could write a
replacement shader that only renders solid objects by using one subshader with
RenderType=Solid [tag](SL-SubShaderTags.html)A reference word which you can
assign to one or more GameObjects to help you identify GameObjects for
scripting purposes. For example, you might define and “Edible” Tag for any
item the player can eat in your game. [More info](Tags.html)  
See in [Glossary](Glossary.html#Tag). The other tag types would not be found
in the replacement shader, so the objects would be not rendered. Or you could
write several subshaders for different “RenderType” tag values. Incidentally,
all built-in **Shader objects** An instance of the Shader class, a Shader
object is container for shader programs and GPU instructions, and information
that tells Unity how to use them. Use them with materials to determine the
appearance of your scene. [More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject) have a “RenderType” tag set.

## Lit shader replacement

When using shader replacement the scene is rendered using the render path that
is configured on the camera. This means that the shader used for replacement
can contain shadow and lighting passes (you can use surface shaders for shader
replacement). This can be useful for doing rendering of special effects and
scene debugging.

## Shader replacement tags in built-in shaders

All built-in shaders have a “**RenderType** ” tag set that can be used when
rendering with replaced shaders. Tag values are the following:

  * **Opaque** : most of the shaders ([Normal](shader-NormalFamily.html)The direction perpendicular to the surface of a mesh, represented by a Vector. Unity uses normals to determine object orientation and apply shading. [More info](scripting-vectors.html)  
See in [Glossary](Glossary.html#Normal), [Self Illuminated](shader-
SelfIllumFamily.html), [Reflective](shader-ReflectiveFamily.html), terrain
shaders).

  * **Transparent** : most semitransparent shaders ([Transparent](shader-TransparentFamily.html), Particle, Font, terrain additive pass shaders).
  * **TransparentCutout** : masked transparency shaders ([Transparent Cutout](shader-TransparentCutoutFamily.html), two pass vegetation shaders).
  * **Background** : **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) shaders.

  * **Overlay** : Halo, Flare shaders.
  * **TreeOpaque** : **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) engine tree bark.

  * **TreeTransparentCutout** : terrain engine tree leaves.
  * **TreeBillboard** : terrain engine billboarded trees.
  * **Grass** : terrain engine grass.
  * **GrassBillboard** : terrain engine billboarded grass.

## Built-in scene depth/normals texture

A Camera has a built-in capability to render depth or depth+normals texture,
if you need that in some of your effects. See [Camera Depth Texture](SL-
CameraDepthTexture.html) page. Note that in some cases (depending on the
hardware), the depth and depth+normals textures can internally be rendered
using shader replacement. So it is important to have the correct
“**RenderType** ” tag in your shaders.

## Code Example

Your Start() function specifies the replacement shaders:

    
    
    void Start() {
        camera.SetReplacementShader (EffectShader, "RenderType");
    }
    

This requests that the EffectShader will use the RenderType key. The
EffectShader will have key-value tags for each RenderType that you want. The
Shader will look something like:

    
    
    Shader "EffectShader" {
         SubShader {
             Tags { "RenderType"="Opaque" }
             Pass {
                 ...
             }
         }
         SubShader {
             Tags { "RenderType"="SomethingElse" }
             Pass {
                 ...
             }
         }
     ...
     }
    

SetReplacementShader will look through all the objects in the scene and,
instead of using their normal shader, use the first subshader which has a
matching value for the specified key. In this example, any objects whose
shader has Rendertype=“Opaque” tag will be replaced by first subshader in
EffectShader, any objects with RenderType=“SomethingElse” shader will use
second replacement subshader and so one. Any objects whose shader does not
have a matching tag value for the specified key in the replacement shader will
not be rendered.

[](Shader-Autodesk-Interactive.html)

Autodesk Interactive shader in the Built-In Render Pipeline

[](writing-shaders-birp.html)

Writing custom shaders in the Built-In Render Pipeline

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

