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

#  [Renderer](Renderer.html).bounds

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

public [Bounds](Bounds.html) bounds;

### Description

The bounding box of the renderer in world space.

This is the axis-aligned bounding box fully enclosing the object in world
space.  
  
Using `bounds` is convenient to make rough approximations about the object's
location and its extents. For example, the `center` property is often a more
precise approximation to the center of the object than
[Transform.position](Transform-position.html), especially if the object is not
symmetrical.  
  
[Mesh.bounds](Mesh-bounds.html) and [localBounds](Renderer-localBounds.html)
are similar but they return the bounds in local space.  
  
You can override the default bounding box by setting your own world space
bounding box. This is mostly useful when the renderer uses a shader that does
custom vertex deformations, and the default bounding box is not accurate.  
  
When you set custom world bounds, the renderer bounding volume no longer
automatically tracks Transform component changes. If there is a local space
bounding volume override ([localBounds](Renderer-localBounds.html)) active at
the same time, it is ignored and the custom world space bounds are used. Use
[ResetBounds](Renderer.ResetBounds.html) to remove the custom bounds override.
Note that the custom world bounds value is not saved into scenes or prefabs
and has to be set from a script at runtime.

    
    
    using UnityEngine;  
      
    public class DrawRendererBounds : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draws a wireframe box around the selected object,
        // indicating world space bounding volume.
        public void OnDrawGizmosSelected()
        {
            var r = GetComponent<[Renderer](Renderer.html)>();
            if (r == null)
                return;
            var bounds = r.bounds;
            [Gizmos.matrix](Gizmos-matrix.html) = [Matrix4x4.identity](Matrix4x4-identity.html);
            [Gizmos.color](Gizmos-color.html) = [Color.blue](Color-blue.html);
            [Gizmos.DrawWireCube](Gizmos.DrawWireCube.html)(bounds.center, bounds.extents * 2);
        }
    }
    

Additional resources: [ResetBounds](Renderer.ResetBounds.html),
[localBounds](Renderer-localBounds.html), [Bounds](Bounds.html),
[Mesh.bounds](Mesh-bounds.html).

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

