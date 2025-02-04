[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/svt-use-in-shader-graph.html)
  * [中文](/cn/current/Manual/svt-use-in-shader-graph.html)
  * [日本語](/ja/current/Manual/svt-use-in-shader-graph.html)
  * [한국어](/kr/current/Manual/svt-use-in-shader-graph.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/svt-use-in-shader-graph.html)
  * [中文](/cn/current/Manual/svt-use-in-shader-graph.html)
  * [日本語](/ja/current/Manual/svt-use-in-shader-graph.html)
  * [한국어](/kr/current/Manual/svt-use-in-shader-graph.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Texture optimization](TextureLoading.html)
  * [Streaming Virtual Texturing](svt-streaming-virtual-texturing.html)
  * Using Streaming Virtual Texturing in Shader Graph

[](svt-enable-in-project.html)

Enabling Streaming Virtual Texturing in your project

[](svt-cache-management.html)

Cache Management for Virtual Texturing

# Using Streaming Virtual Texturing in Shader Graph

This feature is experimental and not ready for production use. The feature and
documentation might be changed or removed in the future.

You can use Streaming Virtual Texturing (SVT) with **shaders** A program that
runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) you create in [Shader
Graph](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest). Before
you begin, you must [enable Virtual Texturing in your project](svt-enable-in-
project.html). The built-in [High Definition Render
Pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-
definition@latest) shaders (such as Lit and Unlit) don’t support SVT.

To use SVT to stream a texture, you must add the texture to a [Virtual Texture
Property](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Property-
Types.html%23virtual-texture). A Virtual Texture Property defines a stack of
related textures. To sample these textures, you connect the Virtual Texture
Property to a [Sample Virtual Texture
node](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest/index.html?subfolder=/manual/Sample-
Virtual-Texture-Node.html). The Sample Virtual Texture node takes one UV
coordinate as the input, and uses that UV coordinate to sample all of the
textures.

You should combine textures into the same Virtual Texture Property where
possible. This is because it’s more efficient to sample multiple textures that
are part of the same Virtual Texture Property than to sample multiple Virtual
Texture Properties.

When you use a Sample Virtual Texture node in the fragment stage, SVT
automatically streams in texture tiles based on the UVs it sampled. For this
to work, the Sample Virtual Texture node outputs the tile ID it reads from
into a render target. To turn this off, open the node settings and disable
**Automatic Streaming**. For more information, see [How Streaming Virtual
Texturing works](svt-how-it-works.html).

To use a Sample Virtual Texture node in the vertex stage, you first need to
disable **Automatic Streaming** on the Sample Virtual Texture node, and then
select the ****Lod** The _Level Of Detail_ (LOD) technique is an optimization
that reduces the number of triangles that Unity has to render for a GameObject
when its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) Level** mode. You must then use a script
to manually request that SVT loads the tiles. To do this, use the
[`VirtualTexturing.Streaming.RequestRegion`](../ScriptReference/Rendering.VirtualTexturing.Streaming.RequestRegion.html)
method as follows:

    
    
    VirtualTexturing.Streaming.RequestRegion(Material, Stack ID, Rect, mipmap, numMips)
    

You can use this method to load any tiles that aren’t yet visible, which
allows you to do things like build a prefetching system. You need to call this
method every frame, otherwise the system assumes that the tiles are no longer
necessary, and potentially evicts them when it streams other tiles.

![This example shows a Virtual Texture Property connected to a Sample Virtual
Texture node in Shader Graph.](../uploads/Main/svt-use-in-shader-graph01.png)
This example shows a Virtual Texture Property connected to a Sample Virtual
Texture node in Shader Graph.

## Shader Graph compatibility

  * You must assign all texture slots of the Virtual Texture Property in Shader Graph.

  * SVT copies each unique combination of textures you assign to a Virtual Texture Property to a unique section of the streaming virtual texture. Therefore, if you use many different combinations of textures in a Virtual Texture Property, it might increase your project build size because each combination is stored separately.

  * There are some limitations when you use the Sample Virtual Texture node in Shader Graph.

    * You cannot use the Sample Virtual Texture node in a Decal graph or on Transparent shaders. If you use the Sample Virtual Texture node in either of these ways, the node uses standard 2D texture sampling instead.
    * Automatic virtual streaming doesn’t work when you use it in the vertex stage of a shader. By default, the Sample Virtual Texture node doesn’t connect to vertex slots in a Shader Graph. To sample a virtual texture stack in the vertex stage, you must set up manual streaming for that texture. To do this, set the **Lod Mode** to **Lod Level** , and disable **Automatic Streaming** in the node settings. You also need to write a C# script that drives data requests for this texture. For more information, see [`VirtualTexturing.Streaming.RequestRegion`](../ScriptReference/Rendering.VirtualTexturing.Streaming.RequestRegion.html).
    * Some **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) or graph settings might be
incompatible with virtual texture streaming. If the Sample Virtual Texture
node doesn’t work with the current configuration, Shader Graph displays a
warning message in the node settings, and the node uses standard 2D texture
sampling instead.

[](svt-enable-in-project.html)

Enabling Streaming Virtual Texturing in your project

[](svt-cache-management.html)

Cache Management for Virtual Texturing

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

