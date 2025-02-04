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

# Gizmos

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Gizmos are used to give visual debugging or setup aids in the Scene view.

All gizmo drawing has to be done in either
[MonoBehaviour.OnDrawGizmos](MonoBehaviour.OnDrawGizmos.html) or
[MonoBehaviour.OnDrawGizmosSelected](MonoBehaviour.OnDrawGizmosSelected.html)
functions of the script.
[MonoBehaviour.OnDrawGizmos](MonoBehaviour.OnDrawGizmos.html) is called when
the Scene view or Game view is repainted. All gizmos that render in
[MonoBehaviour.OnDrawGizmos](MonoBehaviour.OnDrawGizmos.html) are pickable.
[MonoBehaviour.OnDrawGizmosSelected](MonoBehaviour.OnDrawGizmosSelected.html)
is called only if the object the script is attached to is selected.

### Static Properties

[color](Gizmos-color.html)| Sets the Color of the gizmos that are drawn next.  
---|---  
[exposure](Gizmos-exposure.html)| Set a texture that contains the exposure
correction for LightProbe gizmos. The value is sampled from the red channel in
the middle of the texture.  
[matrix](Gizmos-matrix.html)| Sets the Matrix4x4 that the Unity Editor uses to
draw Gizmos.  
[probeSize](Gizmos-probeSize.html)| Set a scale for Light Probe gizmos. This
scale will be used to render the spherical harmonic preview spheres.  
  
### Static Methods

[CalculateLOD](Gizmos.CalculateLOD.html)| Determines the appropriate level of
detail for a gizmo in the Scene view at a specified position with a specified
radius.  
---|---  
[DrawCube](Gizmos.DrawCube.html)| Draw a solid box at center with size.  
[DrawFrustum](Gizmos.DrawFrustum.html)| Draw a camera frustum using the
currently set Gizmos.matrix for its location and rotation.  
[DrawGUITexture](Gizmos.DrawGUITexture.html)| Draw a texture in the Scene.  
[DrawIcon](Gizmos.DrawIcon.html)| Draw an icon at a position in the Scene
view.  
[DrawLine](Gizmos.DrawLine.html)| Draws a line starting at from towards to.  
[DrawLineList](Gizmos.DrawLineList.html)| Draws multiple lines between pairs
of points.  
[DrawLineStrip](Gizmos.DrawLineStrip.html)| Draws a line between each point in
the supplied span.  
[DrawMesh](Gizmos.DrawMesh.html)| Draws a mesh.  
[DrawRay](Gizmos.DrawRay.html)| Draws a ray starting at from to from +
direction.  
[DrawSphere](Gizmos.DrawSphere.html)| Draws a solid sphere with center and
radius.  
[DrawWireCube](Gizmos.DrawWireCube.html)| Draw a wireframe box with center and
size.  
[DrawWireMesh](Gizmos.DrawWireMesh.html)| Draws a wireframe mesh.  
[DrawWireSphere](Gizmos.DrawWireSphere.html)| Draws a wireframe sphere with
center and radius.  
  
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

