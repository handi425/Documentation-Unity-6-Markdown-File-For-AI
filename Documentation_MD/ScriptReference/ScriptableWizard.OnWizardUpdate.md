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

#  [ScriptableWizard](ScriptableWizard.html).OnWizardUpdate()

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

This is called when the wizard is opened or whenever the user changes
something in the wizard.

This allows you to set the [helpString](ScriptableWizard-helpString.html),
[errorString](ScriptableWizard-errorString.html) and enable/disable the Create
button via [isValid](ScriptableWizard-isValid.html). Also it lets you change
labels (for timers i.e.) or buttons when the wizard is being shown  
  
Additional resources:
[ScriptableWizard.DisplayWizard](ScriptableWizard.DisplayWizard.html)  
  
![](../StaticFiles/ScriptRefImages/CloneObjects.png)  
_ScriptableWizard window for cloning a Game Object._

    
    
    // Simple Wizard that clones an object several times.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Collections;  
      
    public class CloneObjects : [ScriptableWizard](ScriptableWizard.html)
    {
        public [GameObject](GameObject.html) objectToCopy = null;
        public int numberOfCopies = 2;
        [[MenuItem](MenuItem.html)("Example/Clone objects")]
        static void CreateWindow()
        {
            // Creates the wizard for display
            [ScriptableWizard.DisplayWizard](ScriptableWizard.DisplayWizard.html)("Clone an object.", typeof(CloneObjects), "Clone!");
        }  
      
        void OnWizardUpdate()
        {
            helpString = "Clones an object a number of times and move the cloned objects to the origin";
            if (!objectToCopy)
            {
                errorString = "Please assign an object";
                isValid = false;
            }
            else
            {
                errorString = "";
                isValid = true;
            }
        }  
      
        void OnWizardCreate()
        {
            for (int i = 0; i < numberOfCopies; i++)
                Instantiate(objectToCopy, [Vector3.zero](Vector3-zero.html), [Quaternion.identity](Quaternion-identity.html));
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

