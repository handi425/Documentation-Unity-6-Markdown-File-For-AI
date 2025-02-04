[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dots-instancing-shaders-declare.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders-declare.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders-declare.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders-declare.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dots-instancing-shaders-declare.html)
  * [中文](/cn/current/Manual/dots-instancing-shaders-declare.html)
  * [日本語](/ja/current/Manual/dots-instancing-shaders-declare.html)
  * [한국어](/kr/current/Manual/dots-instancing-shaders-declare.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
  * [BatchRendererGroup API in URP](batch-renderer-group.html)
  * [Writing custom shaders for the BatchRendererGroup API](batch-renderer-group-writing-shaders.html)
  * Declare DOTS Instancing properties in a custom shader in URP

[](dots-instancing-shaders-support.html)

Support DOTS Instancing in a a custom shader in URP

[](dots-instancing-shaders-access.html)

Access DOTS Instancing properties in a custom shader

# Declare DOTS Instancing properties in a custom shader in URP

To load instance data, such as transform matrices, the **shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) needs to define DOTS Instanced
properties. Below is an example of a simple DOTS Instanced property block:

    
    
    UNITY_DOTS_INSTANCING_START(MaterialPropertyMetadata)
        UNITY_DOTS_INSTANCED_PROP(float4, Color)
    UNITY_DOTS_INSTANCING_END(MaterialPropertyMetadata)
    

To mark the beginning and end of the property block, use the
`UNITY_DOTS_INSTANCING_START` and `UNITY_DOTS_INSTANCING_END` macros followed
by the name of the block. The example uses the name
`MaterialPropertyMetadata`. There are three allowed block names:

  * BuiltinPropertyMetadata
  * MaterialPropertyMetadata
  * UserPropertyMetadata

The shader can declare one of each, so a DOTS Instanced shader can have
between zero and three of such blocks. Unity-defined shader code doesn’t use
UserPropertyMetadata so this name is guaranteed to be free for you to use. URP
and HDRP define BuiltinPropertyMetadata for every shader they provide and
define MaterialPropertyMetadata for most of them too, so it’s best practice to
use UserPropertyMetadata. Your custom shaders can use all three possible
names, even all at once.

The block can contain any number of DOTS Instanced property definitions
formatted like:

    
    
    UNITY_DOTS_INSTANCED_PROP(PropertyType, PropertyName)
    

`PropertyType` can be any HLSL built-in type (like uint, float4, float4x4, or
int2x4) except a bool vector, and `PropertyName` is the name of the DOTS
Instanced property. DOTS Instanced properties are completely separate from
[regular material properties](SL-Properties.html), and you can give them the
same name as another regular material property. This is possible because the
`UNITY_DOTS_INSTANCED_PROP` macro generates special constant names which Unity
recognizes that don’t conflict with other property names. Shaders that Unity
provides give DOTS Instanced properties the same names as regular material
properties, but you don’t need to follow this convention.

Internally, Unity provides the shader with a 32-bit integer metadata value for
every DOTS Instanced property the shader declares. Unity sets the metadata
value when your code makes a
[BatchRendererGroup.AddBatch](../ScriptReference/Rendering.BatchRendererGroup.AddBatch.html)
call to create the batch associated with the draw. The metadata value defaults
to `0` if Unity doesn’t set it. The shader also has access to
`ByteAddressBuffer unity_DOTSInstanceData` which Unity sets to the
GraphicsBuffer you pass as an argument to `BatchRendererGroup.AddBatch`. This
buffer is typically where the shader loads the instance data from. Multiple
batches can share a single GraphicsBuffer, but it is also possible for each
batch to use its own separate GraphicsBuffer for `unity_DOTSInstanceData`.

**Note** : Unity doesn’t provide any DOTS Instanced data automatically. It’s
your responsibility to make sure that the `unity_DOTSInstanceData` buffer of
each batch contains the correct data. Instance data must include many
properties that are Unity normally provides for **GameObjects** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), such as transform matrices,
**light probe** Light probes store information about how light passes through
space in your scene. A collection of light probes arranged within a given
space can improve lighting on moving objects and static LOD scenery within
that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) coefficients, and **lightmap** A
pre-rendered texture that contains the effects of light sources on static
objects in the scene. Lightmaps are overlaid on top of scene geometry to
create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) texture coordinates.

[](dots-instancing-shaders-support.html)

Support DOTS Instancing in a a custom shader in URP

[](dots-instancing-shaders-access.html)

Access DOTS Instancing properties in a custom shader

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

