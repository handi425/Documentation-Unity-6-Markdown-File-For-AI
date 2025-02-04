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

#  [Vector2](Vector2.html).MoveTowards

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

public static [Vector2](Vector2.html) MoveTowards([Vector2](Vector2.html)
current, [Vector2](Vector2.html) target, float maxDistanceDelta);

### Description

Moves a point `current` towards `target`.

This is essentially the same as [Vector2.Lerp](Vector2.Lerp.html) but instead
the function will ensure that the distance never exceeds `maxDistanceDelta`.
Negative values of `maxDistanceDelta` pushes the vector away from `target`.

    
    
    using UnityEngine;  
      
    // 2D MoveTowards example
    // Move the sprite to where the mouse is clicked
    //
    // Set speed to -1.0f and the sprite will move
    // away from the mouse click position forever  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private float speed = 10.0f;
        private [Vector2](Vector2.html) target;
        private [Vector2](Vector2.html) position;
        private [Camera](Camera.html) cam;  
      
        void Start()
        {
            target = new [Vector2](Vector2.html)(0.0f, 0.0f);
            position = gameObject.transform.position;  
      
            cam = [Camera.main](Camera-main.html);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            float step = speed * [Time.deltaTime](Time-deltaTime.html);  
      
            // move sprite towards the target location
            transform.position = [Vector2.MoveTowards](Vector2.MoveTowards.html)(transform.position, target, step);
        }  
      
        void OnGUI()
        {
            [Event](Event.html) currentEvent = [Event.current](Event-current.html);
            [Vector2](Vector2.html) mousePos = new [Vector2](Vector2.html)();
            [Vector2](Vector2.html) point = new [Vector2](Vector2.html)();  
      
            // compute where the mouse is in world space
            mousePos.x = currentEvent.mousePosition.x;
            mousePos.y = cam.pixelHeight - currentEvent.mousePosition.y;
            point = cam.ScreenToWorldPoint(new [Vector3](Vector3.html)(mousePos.x, mousePos.y, 0.0f));  
      
            if ([Input.GetMouseButtonDown](Input.GetMouseButtonDown.html)(0))
            {
                // set the target to the mouse click location
                target = point;
            }
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

