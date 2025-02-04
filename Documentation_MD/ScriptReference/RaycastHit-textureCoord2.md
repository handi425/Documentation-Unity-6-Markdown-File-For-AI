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

#  [RaycastHit](RaycastHit.html).textureCoord2

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

public [Vector2](Vector2.html) textureCoord2;

### Description

The secondary uv texture coordinate at the impact point.

This can be used for 3D texture painting or drawing bullet marks. If the
collider is not a mesh collider, [Vector2.zero](Vector2-zero.html) will be
returned. If the mesh contains no secondary uv set, the uv of the primary uv
set will be returned. This property can be accessed off the main thread.  
  
**Note:** A [textureCoord2](RaycastHit-textureCoord2.html) requires the
collider to be a [MeshCollider](MeshCollider.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Attach this script to a camera and it will paint black pixels in 3D
        // on whatever the user clicks. Make sure the mesh you want to paint
        // on has a mesh collider attached.  
      
        [Camera](Camera.html) cam;  
      
        void Start()
        {
            cam = GetComponent<[Camera](Camera.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Only when we press the mouse
            if (![Input.GetMouseButton](Input.GetMouseButton.html)(0))
            {
                return;
            }  
      
            // Only if we hit something, do we continue
            [RaycastHit](RaycastHit.html) hit;
            if (![Physics.Raycast](Physics.Raycast.html)(cam.ScreenPointToRay([Input.mousePosition](Input-mousePosition.html)), out hit))
            {
                return;
            }  
      
            // Just in case, also make sure the collider also has a renderer
            // material and texture. Also we should ignore primitive colliders.
            [Renderer](Renderer.html) rend = hit.transform.GetComponent<[Renderer](Renderer.html)>();  
      
            [MeshCollider](MeshCollider.html) meshCollider = hit.collider as [MeshCollider](MeshCollider.html);  
      
            if (rend == null || rend.sharedMaterial == null ||
                rend.sharedMaterial.mainTexture == null || meshCollider == null)
            {
                return;
            }  
      
            // Now draw a pixel where we hit the object
            [Texture2D](Texture2D.html) tex = rend.material.mainTexture as [Texture2D](Texture2D.html);
            [Vector2](Vector2.html) pixelUV = hit.textureCoord2;
            pixelUV.x *= tex.width;
            pixelUV.y *= tex.height;  
      
            tex.SetPixel([Mathf.FloorToInt](Mathf.FloorToInt.html)(pixelUV.x), [Mathf.FloorToInt](Mathf.FloorToInt.html)(pixelUV.y), [Color.black](Color-black.html));  
      
            tex.Apply();
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

