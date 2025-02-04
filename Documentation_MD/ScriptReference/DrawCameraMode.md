[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# DrawCameraMode

enumeration

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Drawing modes for [Handles.DrawCamera](Handles.DrawCamera.html).

### Properties

[UserDefined](DrawCameraMode.UserDefined.html)| A custom mode defined by the
user.  
---|---  
[Normal](DrawCameraMode.Normal.html)| Draw the camera like it would be drawn
in-game. This uses the clear flags of the camera.  
[Textured](DrawCameraMode.Textured.html)| Draw the camera textured with
selection wireframe and no background clearing.  
[Wireframe](DrawCameraMode.Wireframe.html)| Draw the camera in wireframe and
no background clearing.  
[TexturedWire](DrawCameraMode.TexturedWire.html)| Draw the camera where all
objects have a wireframe overlay. and no background clearing.  
[ShadowCascades](DrawCameraMode.ShadowCascades.html)| The camera is set to
draw directional light shadow map cascades.  
[RenderPaths](DrawCameraMode.RenderPaths.html)| The camera is set to draw
color coded render paths.  
[AlphaChannel](DrawCameraMode.AlphaChannel.html)| The camera is set to display
the alpha channel of the rendering.  
[Overdraw](DrawCameraMode.Overdraw.html)| The camera is set to display Scene
overdraw, with brighter colors indicating more overdraw.  
[Mipmaps](DrawCameraMode.Mipmaps.html)| The camera is set to display the
texture resolution, with a red tint indicating resolution that is too high,
and a blue tint indicating texture sizes that could be higher.  
[DeferredDiffuse](DrawCameraMode.DeferredDiffuse.html)| Draw diffuse color of
Deferred Shading G-buffer.  
[DeferredSpecular](DrawCameraMode.DeferredSpecular.html)| Draw specular color
of Deferred Shading G-buffer.  
[DeferredSmoothness](DrawCameraMode.DeferredSmoothness.html)| Draw smoothness
value of Deferred Shading G-buffer.  
[DeferredNormal](DrawCameraMode.DeferredNormal.html)| Draw world space normal
of Deferred Shading G-buffer.  
[RealtimeCharting](DrawCameraMode.RealtimeCharting.html)| Draw objects with
different colors for each real-time chart (UV island).  
[Systems](DrawCameraMode.Systems.html)| Draw objects with different color for
each GI system.  
[RealtimeAlbedo](DrawCameraMode.RealtimeAlbedo.html)| Draw objects with the
Enlighten Realtime Global Illumination albedo component only.  
[RealtimeEmissive](DrawCameraMode.RealtimeEmissive.html)| Draw objects with
the Enlighten Realtime Global Illumination emission component only.  
[RealtimeIndirect](DrawCameraMode.RealtimeIndirect.html)| Draw objects with
the Enlighten Realtime Global Illumination indirect light only.  
[RealtimeDirectionality](DrawCameraMode.RealtimeDirectionality.html)| Draw
objects with the Enlighten Realtime Global Illumination directionality
component only.  
[BakedLightmap](DrawCameraMode.BakedLightmap.html)| Draw objects with the
baked lightmap only.  
[Clustering](DrawCameraMode.Clustering.html)| Draw with different colors for
each cluster.  
[LitClustering](DrawCameraMode.LitClustering.html)| Draw lit clusters.  
[ValidateAlbedo](DrawCameraMode.ValidateAlbedo.html)| The camera is set to
draw a physically based, albedo validated rendering.  
[ValidateMetalSpecular](DrawCameraMode.ValidateMetalSpecular.html)| The camera
is set to draw a physically based, metal or specular validated rendering.  
[ShadowMasks](DrawCameraMode.ShadowMasks.html)| The camera is set to display
colored ShadowMasks, coloring light gizmo with the same color.  
[LightOverlap](DrawCameraMode.LightOverlap.html)| The camera is set to show in
red static lights that fall back to 'static' because more than four light
volumes are overlapping.  
[BakedAlbedo](DrawCameraMode.BakedAlbedo.html)| Draw objects with the baked
albedo component only.  
[BakedEmissive](DrawCameraMode.BakedEmissive.html)| Draw objects with the
baked emission component only.  
[BakedDirectionality](DrawCameraMode.BakedDirectionality.html)| Draw objects
with the baked directionality component only.  
[BakedTexelValidity](DrawCameraMode.BakedTexelValidity.html)| Draw objects
with baked texel validity only.  
[BakedIndices](DrawCameraMode.BakedIndices.html)| Draw objects with baked
indices only.  
[BakedCharting](DrawCameraMode.BakedCharting.html)| Draw objects with
different colors for each baked chart (UV island).  
[SpriteMask](DrawCameraMode.SpriteMask.html)| The camera is set to display
SpriteMask and SpriteRenderer with SpriteRenderer.maskInteraction set.  
[BakedUVOverlap](DrawCameraMode.BakedUVOverlap.html)| Draw objects with
overlapping lightmap texels highlighted.  
[TextureStreaming](DrawCameraMode.TextureStreaming.html)| The camera is set to
run in texture streaming debug mode.  
[BakedLightmapCulling](DrawCameraMode.BakedLightmapCulling.html)| Draw objects
with visible lightmap texels highlighted.  
[GIContributorsReceivers](DrawCameraMode.GIContributorsReceivers.html)| Draw
Mesh Renderers and Terrains in different colors to show their
StaticEditorFlags.ContributeGI / ReceiveGI properties. With default colors:
Yellow means 'ContributeGI' is off. Blue means that 'ContributeGI' is on and
the object receives GI from lightmaps. Additional resources:
ReceiveGI.Lightmaps Red means that 'ContributeGI' is on, but that the object
receives GI from Light Probes instead. Additional resources:
ReceiveGI.LightProbes.All colors can be adjusted under Preferences > Colors.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

