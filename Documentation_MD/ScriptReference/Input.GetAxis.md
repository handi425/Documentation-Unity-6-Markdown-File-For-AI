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

#  [Input](Input.html).GetAxis

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

public static float GetAxis(string axisName);

### Description

Returns the value of the virtual axis identified by `axisName`.

**Note: This API is part of the legacy** `Input` **class, and not recommended
for new projects. The documentation is provided here to support legacy
projects that use the old Input Manager and Input class. For new projects you
should use the newer and Input System Package**. ([read
more](../Manual/Input.html)).  
  
The value will be in the range -1...1 for keyboard and joystick input devices.  
  
The meaning of this value depends on the type of input control, for example
with a joystick's horizontal axis a value of 1 means the stick is pushed all
the way to the right and a value of -1 means it's all the way to the left; a
value of 0 means the joystick is in its neutral position.  
  
If the axis is mapped to the mouse, the value is different and will not be in
the range of -1...1. Instead it'll be the current mouse delta multiplied by
the axis sensitivity. Typically a positive value means the mouse is moving
right/down and a negative value means the mouse is moving left/up.  
  
This is frame-rate independent; you do not need to be concerned about varying
frame-rates when using this value.  
  
To set up your input or view the options for `axisName`, go to **Edit** >
**Project Settings** > **Input Manager**. This brings up the Input Manager.
Expand **Axis** to see the list of your current inputs. You can use one of
these as the `axisName`. To rename the input or change the positive button
etc., expand one of the options, and change the name in the **Name** field or
**Positive Button** field. Also, change the **Type** to **Joystick Axis**. To
add a new input, add 1 to the number in the **Size** field.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // A very simplistic car driving on the x-z plane.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float speed = 10.0f;
        public float rotationSpeed = 100.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Get the horizontal and vertical axis.
            // By default they are mapped to the arrow keys.
            // The value is in the range -1 to 1
            float translation = [Input.GetAxis](Input.GetAxis.html)("Vertical") * speed;
            float rotation = [Input.GetAxis](Input.GetAxis.html)("Horizontal") * rotationSpeed;  
      
            // Make it move 10 meters per second instead of 10 meters per frame...
            translation *= [Time.deltaTime](Time-deltaTime.html);
            rotation *= [Time.deltaTime](Time-deltaTime.html);  
      
            // Move translation along the object's z-axis
            transform.Translate(0, 0, translation);  
      
            // [Rotate](UIElements.Rotate.html) around our y-axis
            transform.Rotate(0, rotation, 0);
        }
    }
    
    
    
    using UnityEngine;
    using System.Collections;  
      
    // Performs a mouse look.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        float horizontalSpeed = 2.0f;
        float verticalSpeed = 2.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Get the mouse delta. This is not in the range -1...1
            float h = horizontalSpeed * [Input.GetAxis](Input.GetAxis.html)("Mouse X");
            float v = verticalSpeed * [Input.GetAxis](Input.GetAxis.html)("Mouse Y");  
      
            transform.Rotate(v, h, 0);
        }
    }
    

**Note:** The Horizontal and Vertical ranges change from 0 to +1 or -1 with
increase/decrease in 0.05f steps. [GetAxisRaw](Input.GetAxisRaw.html) has
changes from 0 to 1 or -1 immediately, so with no steps.

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

