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

# DrawingScope

struct in UnityEditor

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

Disposable helper struct for automatically setting and reverting
[Handles.color](Handles-color.html) and/or [Handles.matrix](Handles-
matrix.html).

This struct allows you to temporarily set the value of
[Handles.color](Handles-color.html) and/or [Handles.matrix](Handles-
matrix.html) inside of a block of code and automatically revert them to their
previous values when the scope is exited.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    // a custom editor that draws a labeled circle around the selected [MeshRenderer](MeshRenderer.html) in the scene view
    [[CustomEditor](CustomEditor.html)(typeof([MeshRenderer](MeshRenderer.html)))]
    public class MeshRendererEditor : [Editor](Editor.html)
    {
        protected virtual void OnSceneGUI()
        {
            [MeshRenderer](MeshRenderer.html) meshRenderer = ([MeshRenderer](MeshRenderer.html))target;  
      
            // get an orientation pointing from the selected object to the camera
            [Vector3](Vector3.html) cameraToTarget = Camera.current.transform.position - meshRenderer.transform.position;
            [Quaternion](Quaternion.html) billboardOrientation = [Quaternion.LookRotation](Quaternion.LookRotation.html)(cameraToTarget, Camera.current.transform.up);  
      
            // set the handle matrix to the target's position, oriented facing the camera
            [Matrix4x4](Matrix4x4.html) matrix = [Matrix4x4.TRS](Matrix4x4.TRS.html)(meshRenderer.transform.position, billboardOrientation, [Vector3.one](Vector3-one.html));
            using (new [Handles.DrawingScope](Handles.DrawingScope.html)([Color.magenta](Color-magenta.html), matrix))
            {
                // draw a magenta circle around the selected object with a label at the top
                [Vector3](Vector3.html) size = meshRenderer.bounds.size;
                float radius = [Mathf.Max](Mathf.Max.html)(size.x, size.y, size.z);
                [Handles.DrawWireArc](Handles.DrawWireArc.html)([Vector3.zero](Vector3-zero.html), [Vector3.forward](Vector3-forward.html), [Vector3.right](Vector3-right.html), 360f, radius);
                [Handles.Label](Handles.Label.html)([Vector3.up](Vector3-up.html) * radius, meshRenderer.name);
            }
        }
    }
    

### Properties

[originalColor](Handles.DrawingScope-originalColor.html)| The value of
Handles.color at the time this DrawingScope was created.  
---|---  
[originalMatrix](Handles.DrawingScope-originalMatrix.html)| The value of
Handles.matrix at the time this DrawingScope was created.  
  
### Constructors

[Handles.DrawingScope](Handles.DrawingScope-ctor.html)| Create a new
DrawingScope and set Handles.color and/or Handles.matrix to the specified
values.  
---|---  
  
### Public Methods

[Dispose](Handles.DrawingScope.Dispose.html)| Automatically reverts
Handles.color and Handles.matrix to their values prior to entering the scope,
when the scope is exited. You do not need to call this method manually.  
---|---  
  
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

