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

#  [ScriptableWizard](ScriptableWizard.html).OnWizardCreate()

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

This is called when the user clicks on the Create button.

Here you perform any final creation/modification actions. After OnCreateWizard
is called, the wizard is automatically closed.  
  
Additional resources:
[ScriptableWizard.DisplayWizard](ScriptableWizard.DisplayWizard.html)  
  
![](../StaticFiles/ScriptRefImages/ScriptableWizardOnWizardCreate.png)  
_ScriptableWizard window for selecting GameObjects of a certain "type"._

    
    
    // [Editor](Editor.html) Script that lets you "Select" all the GameObjects that have a certain [Component](Component.html).  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Collections;  
      
    public class ScriptableWizardOnWizardCreate : [ScriptableWizard](ScriptableWizard.html)
    {
        [[MenuItem](MenuItem.html)("Example/OnWizardCreate example")]
        public static void SelectAllOfTypeMenuIem()
        {
            [ScriptableWizard.DisplayWizard](ScriptableWizard.DisplayWizard.html)(
                "Select objects of type ...",
                typeof(ScriptableWizardOnWizardCreate),
                "Select");
        }  
      
        void OnWizardCreate()
        {
            Object[] objs = FindObjectsOfType(typeof([GameObject](GameObject.html)));
            ArrayList selectionBuilder = new ArrayList();
            foreach ([GameObject](GameObject.html) go in objs)
            {
                if (go.GetComponent<[Camera](Camera.html)>())
                    selectionBuilder.Add(go);
            }
            [Selection.objects](Selection-objects.html) = selectionBuilder.ToArray(typeof([GameObject](GameObject.html))) as [GameObject](GameObject.html)[];
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

