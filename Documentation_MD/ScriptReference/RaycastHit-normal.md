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

#  [RaycastHit](RaycastHit.html).normal

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

public [Vector3](Vector3.html) normal;

### Description

The normal of the surface the ray hit.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Calculate the reflection of a "laser beam" off a clicked object.  
      
        // The object from which the beam is fired. The incoming beam will
        // not be visible if the camera is used for this!
        [Transform](Transform.html) gunObj;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetMouseButton](Input.GetMouseButton.html)(0))
            {
                [RaycastHit](RaycastHit.html) hit;
                [Ray](Ray.html) ray = Camera.main.ScreenPointToRay([Input.mousePosition](Input-mousePosition.html));  
      
                if ([Physics.Raycast](Physics.Raycast.html)(ray, out hit))
                {
                    // Find the line from the gun to the point that was clicked.
                    [Vector3](Vector3.html) incomingVec = hit.point - gunObj.position;  
      
                    // Use the point's normal to calculate the reflection vector.
                    [Vector3](Vector3.html) reflectVec = [Vector3.Reflect](Vector3.Reflect.html)(incomingVec, hit.normal);  
      
                    // Draw lines to show the incoming "beam" and the reflection.
                    [Debug.DrawLine](Debug.DrawLine.html)(gunObj.position, hit.point, [Color.red](Color-red.html));
                    [Debug.DrawRay](Debug.DrawRay.html)(hit.point, reflectVec, [Color.green](Color-green.html));
                }
            }
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

