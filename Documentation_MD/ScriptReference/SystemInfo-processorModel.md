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

#  [SystemInfo](SystemInfo.html).processorModel

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

public static string processorModel;

### Description

Specifies the model name of the processor in the user's device (Read Only).

With `SystemInfo.processorModel` and
[SystemInfo.processorManufacturer](SystemInfo-processorManufacturer.html)
values, you can categorize the devices running Unity applications to gather
accurate performance metrics. You can use this data to test and optimize your
application for improved performance.  
  
Returns `unknown` on WebGL platforms and IOS platforms platforms which don't
support this property.  
  
Additional resources: [SystemInfo.processorManufacturer](SystemInfo-
processorManufacturer.html)

    
    
    using UnityEngine;
    using TMPro;
    public class NewBehaviourScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public TMP_Text DisplayText;
        private string _processorModel;  
      
        void Start()
        {
            _processorModel = [SystemInfo.processorModel](SystemInfo-processorModel.html);
            DisplayText.text = _processorModel;
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

