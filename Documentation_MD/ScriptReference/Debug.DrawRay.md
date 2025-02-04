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

#  [Debug](Debug.html).DrawRay

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

[Switch to Manual](../Manual/class-Debug.html "Go to Debug Component in the
Manual")

## Declaration

public static void DrawRay([Vector3](Vector3.html) start,
[Vector3](Vector3.html) dir, [Color](Color.html) color = Color.white, float
duration = 0.0f, bool depthTest = true);

### Parameters

start | Point in world space where the ray should start.  
---|---  
dir | Direction and length of the ray.  
color | Color of the drawn line.  
duration | How long the line will be visible for (in seconds).  
depthTest | Determines whether objects closer to the camera obscure the line.  
  
### Description

Draws a line from `start` to `start` \+ `dir` in world coordinates.

The `duration` parameter determines how long the line will be visible after
the frame it is drawn. If duration is 0 (the default) then the line is
rendered 1 frame.  
  
If `depthTest` is set to true then the line will be obscured by other objects
in the Scene that are nearer to the camera.  
  
The line will be drawn in the Scene view of the editor. If gizmo drawing is
enabled in the game view, the line will also be drawn there.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Frame update example: Draws a 10 meter long green line from the position for 1 frame.
        void [Update](PlayerLoop.Update.html)()
        {
            [Vector3](Vector3.html) forward = transform.TransformDirection([Vector3.forward](Vector3-forward.html)) * 10;
            [Debug.DrawRay](Debug.DrawRay.html)(transform.position, forward, [Color.green](Color-green.html));
        }
    }
    
    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // [Event](Event.html) callback example: [Debug](Debug.html)-draw all contact points and normals for 2 seconds.
        void OnCollisionEnter([Collision](Collision.html) collision)
        {
            [Debug.DrawRay](Debug.DrawRay.html)(collision.contacts[0].point, collision.contacts[0].normal, [Color.green](Color-green.html), 2, false);
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

