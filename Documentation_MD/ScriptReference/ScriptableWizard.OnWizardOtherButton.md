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

#  [ScriptableWizard](ScriptableWizard.html).OnWizardOtherButton()

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

Allows you to provide an action when the user clicks on the other button.

This is the place where you can implement all the stuff that will be done if
the user clicks the secondary option when calling DisplayWizard.  
  
Additional resources:
[ScriptableWizard.DisplayWizard](ScriptableWizard.DisplayWizard.html)  
  
![](../StaticFiles/ScriptRefImages/ScriptableWizardOnWizardOtherButton.png)  
_ScriptableWizard with an "Other" button, in this case named "Info"._

    
    
    // [Display](Display.html) a window showing the distance between two objects when clicking the Info button.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ScriptableWizardOnWizardOtherButton : [ScriptableWizard](ScriptableWizard.html)
    {
        public [Transform](Transform.html) firstObject = null;
        public [Transform](Transform.html) secondObject = null;  
      
        [[MenuItem](MenuItem.html)("Example/Show OnWizardOtherButton Usage")]
        static void CreateWindow()
        {
            [ScriptableWizard.DisplayWizard](ScriptableWizard.DisplayWizard.html)("Click info to know the distance between the objects",
                typeof(ScriptableWizardOnWizardOtherButton), "Finish!", "Info");
        }  
      
        void OnWizardUpdate()
        {
            if (firstObject == null || secondObject == null)
            {
                isValid = false;
                errorString = "Select the objects you want to measure";
            }
            else
            {
                isValid = true;
                errorString = "";
            }
        }  
      
        // Called when you press the "Info" button.
        void OnWizardOtherButton()
        {
            float distanceObjs = [Vector3.Distance](Vector3.Distance.html)(firstObject.position, secondObject.position);
            [EditorUtility.DisplayDialog](EditorUtility.DisplayDialog.html)(
                "The distance between the objects is: " + distanceObjs + " Units",
                "",
                "OK");
        }  
      
        // Called when you press the "Finish!" button.
        void OnWizardCreate()
        {
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

