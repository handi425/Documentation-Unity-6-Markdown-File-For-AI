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

#  [RaycastHit](RaycastHit.html).textureCoord

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

public [Vector2](Vector2.html) textureCoord;

### Description

The uv texture coordinate at the collision location.

A ray is fired into the Scene. The `textureCoord` is the location where the
ray has hit a collider. `RaycastHit._textureCoord` is a texture coordinate
when a hit occurs. A [Vector2](Vector2.html) zero is returned if no mesh
collider is present in the `GameObject`. This property can be accessed off the
main thread.  
  
**Note:** A [textureCoord](RaycastHit-textureCoord.html) requires the collider
to be a [MeshCollider](MeshCollider.html).

    
    
    // Write black pixels onto the [GameObject](GameObject.html) that is located
    // by the script. The script is attached to the camera.
    // Determine where the collider hits and modify the texture at that point.
    //
    // Note that the [MeshCollider](MeshCollider.html) on the [GameObject](GameObject.html) must have Convex turned off. This allows
    // concave GameObjects to be included in collision in this example.
    //
    // Also to allow the texture to be updated by mouse button clicks it must have the Read/Write
    // Enabled option set to true in its Advanced import settings.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Camera](Camera.html) cam;  
      
        void Start()
        {
            cam = GetComponent<[Camera](Camera.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (![Input.GetMouseButton](Input.GetMouseButton.html)(0))
                return;  
      
            [RaycastHit](RaycastHit.html) hit;
            if (![Physics.Raycast](Physics.Raycast.html)(cam.ScreenPointToRay([Input.mousePosition](Input-mousePosition.html)), out hit))
                return;  
      
            [Renderer](Renderer.html) rend = hit.transform.GetComponent<[Renderer](Renderer.html)>();
            [MeshCollider](MeshCollider.html) meshCollider = hit.collider as [MeshCollider](MeshCollider.html);  
      
            if (rend == null || rend.sharedMaterial == null || rend.sharedMaterial.mainTexture == null || meshCollider == null)
                return;  
      
            [Texture2D](Texture2D.html) tex = rend.material.mainTexture as [Texture2D](Texture2D.html);
            [Vector2](Vector2.html) pixelUV = hit.textureCoord;
            pixelUV.x *= tex.width;
            pixelUV.y *= tex.height;  
      
            tex.SetPixel((int)pixelUV.x, (int)pixelUV.y, [Color.black](Color-black.html));
            tex.Apply();
        }
    }
    

Additional resources: [Physics.Raycast](Physics.Raycast.html),
[Physics.Linecast](Physics.Linecast.html),
[Physics.RaycastAll](Physics.RaycastAll.html).

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

