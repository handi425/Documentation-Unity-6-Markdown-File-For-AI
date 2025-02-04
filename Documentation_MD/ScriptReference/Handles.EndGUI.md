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

#  [Handles](Handles.html).EndGUI

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

public static void EndGUI();

### Description

End a 2D GUI block and get back to the 3D handle GUI.

Additional resources: [Handles.BeginGUI](Handles.BeginGUI.html).  
  
![](../StaticFiles/ScriptRefImages/BeginEndGUI2.png)  
_GUI in the Scene View._

    
    
    // Change the transform values for the selected object.
    // When selected this script starts and the handleExample is managed.
    // The HandlesGUI.BeginGUI() and EndGUI() functions allow the shieldArea
    // to be changed back to five, which is the starting value.  
      
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(HandleExample))]
    class HandleExampleEditor : [Editor](Editor.html)
    {
        protected virtual void OnSceneGUI()
        {
            HandleExample handleExample = (HandleExample)target;  
      
            if (handleExample == null)
            {
                return;
            }  
      
            [Handles.color](Handles-color.html) = [Color.yellow](Color-yellow.html);  
      
            [GUIStyle](GUIStyle.html) style = new [GUIStyle](GUIStyle.html)();
            style.normal.textColor = [Color.green](Color-green.html);  
      
            [Vector3](Vector3.html) position = handleExample.transform.position + [Vector3.up](Vector3-up.html) * 2f;
            string posString = position.ToString();  
      
            [Handles.Label](Handles.Label.html)(position,
                posString + "\nShieldArea: " +
                handleExample.shieldArea.ToString(),
                style
            );  
      
            [Handles.BeginGUI](Handles.BeginGUI.html)();
            if ([GUILayout.Button](GUILayout.Button.html)("Reset Area", [GUILayout.Width](GUILayout.Width.html)(100)))
            {
                handleExample.shieldArea = 5;
            }
            [Handles.EndGUI](Handles.EndGUI.html)();  
      
            [Handles.DrawWireArc](Handles.DrawWireArc.html)(
                handleExample.transform.position,
                handleExample.transform.up,
                -handleExample.transform.right,
                180,
                handleExample.shieldArea);  
      
            handleExample.shieldArea =
                [Handles.ScaleValueHandle](Handles.ScaleValueHandle.html)(handleExample.shieldArea,
                    handleExample.transform.position + handleExample.transform.forward * handleExample.shieldArea,
                    handleExample.transform.rotation,
                    1, [Handles.ConeHandleCap](Handles.ConeHandleCap.html), 1);
        }
    }
    

Add a script that specifies the object that can be animated in the SceneView.

    
    
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class HandleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public float shieldArea = 5.0f;
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

