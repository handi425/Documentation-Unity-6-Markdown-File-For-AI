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

#  [Input](Input.html).GetTouch

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

public static [Touch](Touch.html) GetTouch(int index);

### Parameters

index | The touch input on the device screen.  
---|---  
  
### Returns

**Touch** Touch details in the struct.

### Description

Call [Input.GetTouch](Input.GetTouch.html) to obtain a [Touch](Touch.html)
struct.

**Note: This API is part of the legacy** `Input` **class, and not recommended
for new projects. The documentation is provided here to support legacy
projects that use the old Input Manager and Input class. For new projects you
should use the newer and Input System Package**. ([read
more](../Manual/Input.html)).  
  
[Input.GetTouch](Input.GetTouch.html) returns [Touch](Touch.html) for a
selected screen touch (for example, from a finger or stylus).
[Touch](Touch.html) describes the screen touch. The [index](Input-index.html)
argument selects the screen touch.  
  
[Input.touchCount](Input-touchCount.html) provides the current number of
screen touches. If [Input.touchCount](Input-touchCount.html) is greater than
zero, the [GetTouch](Input.GetTouch.html) [index](Input-index.html) sets which
screen touch to check. [Touch](Touch.html) returns a `struct` with the screen
touch details. Each extra screen touch uses an increasing
[Input.touchCount](Input-touchCount.html).  
  
[GetTouch](Input.GetTouch.html) returns a [Touch](Touch.html) struct. Use zero
to obtain the first screen touch. As an example, [Touch](Touch.html) includes
[position](Input-position.html) in pixels.  
  
No temporary variables are allocated.

    
    
    using UnityEngine;
    using System.Collections;
    using UnityEngine.iOS;  
      
    // [Input.GetTouch](Input.GetTouch.html) example.
    //
    // Attach to an origin based cube.
    // A screen touch moves the cube on an iPhone or iPad.
    // A second screen touch reduces the cube size.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Vector3](Vector3.html) position;
        private float width;
        private float height;  
      
        void Awake()
        {
            width = (float)[Screen.width](Screen-width.html) / 2.0f;
            height = (float)[Screen.height](Screen-height.html) / 2.0f;  
      
            // [Position](UIElements.Position.html) used for the cube.
            position = new [Vector3](Vector3.html)(0.0f, 0.0f, 0.0f);
        }  
      
        void OnGUI()
        {
            // Compute a fontSize based on the size of the screen width.
            GUI.skin.label.fontSize = (int)([Screen.width](Screen-width.html) / 25.0f);  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(20, 20, width, height * 0.25f),
                "x = " + position.x.ToString("f2") +
                ", y = " + position.y.ToString("f2"));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Handle screen touches.
            if ([Input.touchCount](Input-touchCount.html) > 0)
            {
                [Touch](Touch.html) touch = [Input.GetTouch](Input.GetTouch.html)(0);  
      
                // Move the cube if the screen has the finger moving.
                if (touch.phase == [TouchPhase.Moved](TouchPhase.Moved.html))
                {
                    [Vector2](Vector2.html) pos = touch.position;
                    pos.x = (pos.x - width) / width;
                    pos.y = (pos.y - height) / height;
                    position = new [Vector3](Vector3.html)(-pos.x, pos.y, 0.0f);  
      
                    // [Position](UIElements.Position.html) the cube.
                    transform.position = position;
                }  
      
                if ([Input.touchCount](Input-touchCount.html) == 2)
                {
                    touch = [Input.GetTouch](Input.GetTouch.html)(1);  
      
                    if (touch.phase == [TouchPhase.Began](TouchPhase.Began.html))
                    {
                        // Halve the size of the cube.
                        transform.localScale = new [Vector3](Vector3.html)(0.75f, 0.75f, 0.75f);
                    }  
      
                    if (touch.phase == [TouchPhase.Ended](TouchPhase.Ended.html))
                    {
                        // Restore the regular size of the cube.
                        transform.localScale = new [Vector3](Vector3.html)(1.0f, 1.0f, 1.0f);
                    }
                }
            }
        }
    }
    

A second example:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) projectile;
        public [GameObject](GameObject.html) clone;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            for (int i = 0; i < [Input.touchCount](Input-touchCount.html); ++i)
            {
                if ([Input.GetTouch](Input.GetTouch.html)(i).phase == [TouchPhase.Began](TouchPhase.Began.html))
                {
                    clone = Instantiate(projectile, transform.position, transform.rotation) as [GameObject](GameObject.html);
                }
            }
        }
    }
    

A third example:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) particle;
        void [Update](PlayerLoop.Update.html)()
        {
            for (int i = 0; i < [Input.touchCount](Input-touchCount.html); ++i)
            {
                if ([Input.GetTouch](Input.GetTouch.html)(i).phase == [TouchPhase.Began](TouchPhase.Began.html))
                {
                    // Construct a ray from the current touch coordinates
                    [Ray](Ray.html) ray = Camera.main.ScreenPointToRay([Input.GetTouch](Input.GetTouch.html)(i).position);  
      
                    // Create a particle if hit
                    if ([Physics.Raycast](Physics.Raycast.html)(ray))
                    {
                        Instantiate(particle, transform.position, transform.rotation);
                    }
                }
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

