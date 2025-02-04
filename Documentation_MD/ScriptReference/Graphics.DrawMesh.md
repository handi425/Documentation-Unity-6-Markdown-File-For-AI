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

#  [Graphics](Graphics.html).DrawMesh

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

## Declaration

public static void DrawMesh([Mesh](Mesh.html) mesh, [Vector3](Vector3.html)
position, [Quaternion](Quaternion.html) rotation, [Material](Material.html)
material, int layer, [Camera](Camera.html) camera = null, int submeshIndex =
0, [MaterialPropertyBlock](MaterialPropertyBlock.html) properties = null, bool
castShadows = true, bool receiveShadows = true, bool useLightProbes = true);

## Declaration

public static void DrawMesh([Mesh](Mesh.html) mesh, [Vector3](Vector3.html)
position, [Quaternion](Quaternion.html) rotation, [Material](Material.html)
material, int layer, [Camera](Camera.html) camera, int submeshIndex,
[MaterialPropertyBlock](MaterialPropertyBlock.html) properties,
[Rendering.ShadowCastingMode](Rendering.ShadowCastingMode.html) castShadows,
bool receiveShadows = true, [Transform](Transform.html) probeAnchor = null,
bool useLightProbes = true);

## Declaration

public static void DrawMesh([Mesh](Mesh.html) mesh,
[Matrix4x4](Matrix4x4.html) matrix, [Material](Material.html) material, int
layer, [Camera](Camera.html) camera = null, int submeshIndex = 0,
[MaterialPropertyBlock](MaterialPropertyBlock.html) properties = null, bool
castShadows = true, bool receiveShadows = true, bool useLightProbes = true);

## Declaration

public static void DrawMesh([Mesh](Mesh.html) mesh,
[Matrix4x4](Matrix4x4.html) matrix, [Material](Material.html) material, int
layer, [Camera](Camera.html) camera, int submeshIndex,
[MaterialPropertyBlock](MaterialPropertyBlock.html) properties,
[Rendering.ShadowCastingMode](Rendering.ShadowCastingMode.html) castShadows,
bool receiveShadows = true, [Transform](Transform.html) probeAnchor = null,
bool useLightProbes = true);

## Declaration

public static void DrawMesh([Mesh](Mesh.html) mesh,
[Matrix4x4](Matrix4x4.html) matrix, [Material](Material.html) material, int
layer, [Camera](Camera.html) camera, int submeshIndex,
[MaterialPropertyBlock](MaterialPropertyBlock.html) properties,
[Rendering.ShadowCastingMode](Rendering.ShadowCastingMode.html) castShadows,
bool receiveShadows, [Transform](Transform.html) probeAnchor,
[Rendering.LightProbeUsage](Rendering.LightProbeUsage.html) lightProbeUsage,
[LightProbeProxyVolume](LightProbeProxyVolume.html) lightProbeProxyVolume =
null);

### Parameters

mesh | The [Mesh](Mesh.html) to draw.  
---|---  
position | Position of the mesh.  
rotation | Rotation of the mesh.  
matrix | Transformation matrix of the mesh (combines position, rotation and other transformations).  
material |  [Material](Material.html) to use.  
layer |  [Layer](../Manual/Layers.html) the mesh is drawn on.  
camera | If `null` (default), the mesh will be drawn in all cameras. Otherwise it will be rendered in the given Camera only.  
submeshIndex | Which subset of the mesh to draw. This applies only to meshes that are composed of several materials.  
properties | Additional material properties to apply onto material just before this mesh will be drawn. See [MaterialPropertyBlock](MaterialPropertyBlock.html).  
castShadows | Determines whether the mesh can cast shadows.  
receiveShadows | Determines whether the mesh can receive shadows.  
useLightProbes | Should the mesh use light probes?  
probeAnchor | If used, the mesh will use this Transform's position to sample light probes and find the matching reflection probe.  
lightProbeUsage |  [LightProbeUsage](Rendering.LightProbeUsage.html) for the mesh.  
  
### Description

Draw a mesh.

This function is now obsolete. Use
[Graphics.RenderMesh](Graphics.RenderMesh.html) instead.  
  
DrawMesh draws a mesh for one frame. The mesh will be affected by the lights,
can cast and receive shadows and be affected by Projectors - just like it was
part of some game object. It can be drawn for all cameras or just for some
specific camera.  
  
Use DrawMesh in situations where you want to draw large amount of meshes, but
don't want the overhead of creating and managing game objects. Note that
DrawMesh does not draw the mesh immediately; it merely "submits" it for
rendering. The mesh will be rendered as part of normal rendering process. If
you want to draw a mesh immediately, use
[Graphics.DrawMeshNow](Graphics.DrawMeshNow.html).  
  
Because DrawMesh does not draw mesh immediately, modifying material properties
between calls to this function won't make the meshes pick them up. If you want
to draw series of meshes with the same material, but slightly different
properties (e.g. change color of each mesh), use
[MaterialPropertyBlock](MaterialPropertyBlock.html) parameter.  
  
Note that this call will create some internal resources while the mesh is
queued up for rendering. The allocation happens immediately and will be kept
around until the end of frame (if the object was queued for all cameras) or
until the specified camera renders itself.  
  
Additional resources: [Graphics.RenderMesh](Graphics.RenderMesh.html),
[MaterialPropertyBlock](MaterialPropertyBlock.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html) {
        public [Mesh](Mesh.html) mesh;
        public [Material](Material.html) material;
        public void [Update](PlayerLoop.Update.html)() {
            // will make the mesh appear in the [Scene](SceneManagement.Scene.html) at origin position
            [Graphics.DrawMesh](Graphics.DrawMesh.html)(mesh, [Vector3.zero](Vector3-zero.html), [Quaternion.identity](Quaternion-identity.html), material, 0);
        }
    }
    

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

