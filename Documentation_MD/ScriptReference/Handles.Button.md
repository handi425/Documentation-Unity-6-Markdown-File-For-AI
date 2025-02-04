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

#  [Handles](Handles.html).Button

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

public static bool Button([Vector3](Vector3.html) position,
[Quaternion](Quaternion.html) direction, float size, float pickSize,
[Handles.CapFunction](Handles.CapFunction.html) capFunction);

### Parameters

position | The position to draw the button in the space of [Handles.matrix](Handles-matrix.html).  
---|---  
direction | The rotation of the button in the space of [Handles.matrix](Handles-matrix.html).  
size | The visual size of the handle. Use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
pickSize | The size of the button for the purpose of detecting a click. Use [HandleUtility.GetHandleSize](HandleUtility.GetHandleSize.html) if you want a constant screen-space size.  
capFunction | The draw style of the button.  
  
### Returns

**bool** True when the user clicks the button.

### Description

Make a 3D Button.

This button works like one drawn with [GUI.Button](GUI.Button.html), but it
has a 3D position and is drawn by a handle function.  
  
![](../StaticFiles/ScriptRefImages/ButtonHandle.png)  
_Button Handle as a rectangle in the Scene View._  
  
Add the following script to your Assets folder as ButtonExample.cs and add the
ButtonExample component to an object in a Scene.

    
    
    using UnityEngine;  
      
    public class ButtonExample : [MonoBehaviour](MonoBehaviour.html) {}
    

Add the following script to Assets/Editor as ButtonExampleEditor.cs and select
the object with the ButtonExample component.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(ButtonExample)), [CanEditMultipleObjects](CanEditMultipleObjects.html)]
    class ButtonExampleEditor : [Editor](Editor.html)
    {
        protected virtual void OnSceneGUI()
        {
            ButtonExample buttonExample = (ButtonExample)target;  
      
            [Vector3](Vector3.html) position = buttonExample.transform.position + [Vector3.up](Vector3-up.html) * 2f;
            float size = 2f;
            float pickSize = size * 2f;  
      
            if ([Handles.Button](Handles.Button.html)(position, [Quaternion.identity](Quaternion-identity.html), size, pickSize, [Handles.RectangleHandleCap](Handles.RectangleHandleCap.html)))
                [Debug.Log](Debug.Log.html)("The button was pressed!");
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

