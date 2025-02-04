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

#  [Handles](Handles.html).Label

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

public static void Label([Vector3](Vector3.html) position, string text);

## Declaration

public static void Label([Vector3](Vector3.html) position,
[Texture](Texture.html) image);

## Declaration

public static void Label([Vector3](Vector3.html) position,
[GUIContent](GUIContent.html) content);

## Declaration

public static void Label([Vector3](Vector3.html) position, string text,
[GUIStyle](GUIStyle.html) style);

## Declaration

public static void Label([Vector3](Vector3.html) position,
[GUIContent](GUIContent.html) content, [GUIStyle](GUIStyle.html) style);

### Parameters

position | The position in 3D space as seen from the current handle camera.  
---|---  
text | The text to display on the label.  
image | The texture to display on the label.  
content | The text, image, and tooltip for this label.  
style | The style to use for this label. If left out, the `label` style from the current GUISkin is used.  
  
### Description

Creates a text label for a handle that is positioned in 3D space.

Labels have no user interaction and canot be clicked on. Labels are always
rendered in normal style.  
  
![](../StaticFiles/ScriptRefImages/HandlesLabel.png)  
_Label in the Scene view._

    
    
    //This script is not an [Editor](Editor.html) script
    //Attach this script to a [GameObject](GameObject.html) in your [Scene](SceneManagement.Scene.html)  
      
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class HandleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public float shieldArea = 5.0f;  
      
        // Use this for initialization
        void Start()
        {
        }  
      
        // [Update](PlayerLoop.Update.html) is called once per frame
        void [Update](PlayerLoop.Update.html)()
        {
        }
    }
    
    
    
    //Create a folder named "[Editor](Editor.html)" in your project directory, if the directroy does not already have one. Place this script in the [Editor](Editor.html) folder.  
      
    using UnityEngine;
    using System.Collections;
    using [UnityEditor](UnityEditor.html);  
      
    // Create a 180 degrees wire arc with a ScaleValueHandle attached to the disc
    // lets you visualize some info of the transform  
      
    [[CustomEditor](CustomEditor.html)(typeof(HandleExample))]
    class LabelHandle : [Editor](Editor.html)
    {
        void OnSceneGUI()
        {
            HandleExample handleExample = (HandleExample)target;
            if (handleExample == null)
            {
                return;
            }  
      
            [Handles.color](Handles-color.html) = [Color.blue](Color-blue.html);
            [Handles.Label](Handles.Label.html)(handleExample.transform.position + [Vector3.up](Vector3-up.html) * 2,
                handleExample.transform.position.ToString() + "\nShieldArea: " +
                handleExample.shieldArea.ToString());  
      
            [Handles.BeginGUI](Handles.BeginGUI.html)();
            if ([GUILayout.Button](GUILayout.Button.html)("Reset Area", [GUILayout.Width](GUILayout.Width.html)(100)))
            {
                handleExample.shieldArea = 5;
            }
            [Handles.EndGUI](Handles.EndGUI.html)();  
      
    
            [Handles.DrawWireArc](Handles.DrawWireArc.html)(handleExample.transform.position,
                handleExample.transform.up,
                -handleExample.transform.right,
                180,
                handleExample.shieldArea);
            handleExample.shieldArea =
                [Handles.ScaleValueHandle](Handles.ScaleValueHandle.html)(handleExample.shieldArea,
                    handleExample.transform.position + handleExample.transform.forward * handleExample.shieldArea,
                    handleExample.transform.rotation,
                    1,
                    [Handles.ConeHandleCap](Handles.ConeHandleCap.html),
                    1);
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

