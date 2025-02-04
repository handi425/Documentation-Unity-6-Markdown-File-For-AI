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

#  [Transform](Transform.html).localEulerAngles

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

[Switch to Manual](../Manual/class-Transform.html "Go to Transform Component
in the Manual")

public [Vector3](Vector3.html) localEulerAngles;

### Description

The rotation as Euler angles in degrees relative to the parent transform's
rotation.

Euler angles can represent a three dimensional rotation by performing three
separate rotations around individual axes. In Unity these rotations are
performed around the Z axis, the X axis, and the Y axis, in that order.  
  
You can set the rotation of a Quaternion by setting this property, and you can
read the Euler angle values by reading this property.  
  
When using the .eulerAngles property to set a rotation, it is important to
understand that although you are providing X, Y, and Z rotation values to
describe your rotation, those values are not stored in the rotation. Instead,
the X, Y & Z values are converted to the Quaternion's internal format.  
  
When you read the .eulerAngles property, Unity converts the Quaternion's
internal representation of the rotation to Euler angles. Because, there is
more than one way to represent any given rotation using Euler angles, the
values you read back out may be quite different from the values you assigned.
This can cause confusion if you are trying to gradually increment the values
to produce animation.  
  
To avoid these kinds of problems, the recommended way to work with rotations
is to avoid relying on consistent results when reading .eulerAngles
particularly when attempting to gradually increment a rotation to produce
animation. For better ways to achieve this, see the [Quaternion *
operator](Quaternion-operator_multiply.html).  
  
The following example demonstrates the rotation of a GameObject using
eulerAngles based on the Input of the user. The example shows that we never
rely on reading the Quanternion.eulerAngles to increment the rotation, instead
we set it using our Vector3 currentEulerAngles. All rotational changes happen
in the currentEulerAngles variable, which are then applied to the Quaternion
avoiding the problem mentioned above.

    
    
    using UnityEngine;
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        float rotationSpeed = 45;
        [Vector3](Vector3.html) currentEulerAngles;
        float x;
        float y;
        float z;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.X](KeyCode.X.html))) x = 1 - x;
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Y](KeyCode.Y.html))) y = 1 - y;
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Z](KeyCode.Z.html))) z = 1 - z;  
      
            //modifying the [Vector3](Vector3.html), based on input multiplied by speed and time
            currentEulerAngles += new [Vector3](Vector3.html)(x, y, z) * [Time.deltaTime](Time-deltaTime.html) * rotationSpeed;  
      
            //apply the change to the gameObject
            transform.localEulerAngles = currentEulerAngles;
        }  
      
        void OnGUI()
        {
            [GUIStyle](GUIStyle.html) style = new [GUIStyle](GUIStyle.html)();
            style.fontSize = 24;
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(10, 0, 0, 0), "Rotating on X:" + x + " Y:" + y + " Z:" + z, style);  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(10, 50, 0, 0), "Transform.localEulerAngle: " + transform.localEulerAngles, style);
        }
    }
    

Unity automatically converts the angles to and from the rotation stored in
[Transform.localRotation](Transform-localRotation.html).

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

