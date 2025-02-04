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

#  [Renderer](Renderer.html).localBounds

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

public [Bounds](Bounds.html) localBounds;

### Description

The bounding box of the renderer in local space.

This is the axis-aligned bounding box fully enclosing the object in local
space.  
  
For a [SkinnedMeshRenderer](SkinnedMeshRenderer.html), default local bounds
are precomputed based on animations associated with that model, which means
that the bounding box might be much bigger than the mesh itself. When
[SkinnedMeshRenderer.updateWhenOffscreen](SkinnedMeshRenderer-
updateWhenOffscreen.html) is enabled, Unity recomputes the local bounds every
frame.  
  
You can override the default bounding box by setting your own local space
bounding box. This is mostly useful when the renderer uses a shader that does
custom vertex deformations, and the default bounding box is not accurate. Use
[ResetLocalBounds](Renderer.ResetLocalBounds.html) to remove custom bounds
override. Note that the custom local bounds value is not saved into scenes or
prefabs and has to be set from a script at runtime.

    
    
    using UnityEngine;  
      
    public class DrawRendererBounds : [MonoBehaviour](MonoBehaviour.html)
    {
        // Draws a wireframe box around the selected object,
        // indicating local space bounding volume.
        public void OnDrawGizmosSelected()
        {
            var r = GetComponent<[Renderer](Renderer.html)>();
            if (r == null)
                return;
            var bounds = r.localBounds;
            [Gizmos.matrix](Gizmos-matrix.html) = transform.localToWorldMatrix;
            [Gizmos.color](Gizmos-color.html) = [Color.blue](Color-blue.html);
            [Gizmos.DrawWireCube](Gizmos.DrawWireCube.html)(bounds.center, bounds.extents * 2);
        }
    }
    

Additional resources: [ResetLocalBounds](Renderer.ResetLocalBounds.html),
[bounds](Renderer-bounds.html), [Bounds](Bounds.html).

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

