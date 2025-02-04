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

#  [PlayerPrefs](PlayerPrefs.html).SetInt

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

public static void SetInt(string key, int value);

### Description

Sets a single integer value for the preference identified by the given key.
You can use [PlayerPrefs.GetInt](PlayerPrefs.GetInt.html) to retrieve this
value.

The following example passes the `KeyName` and `Value` variables to a function
called `SetInt`. The function uses the `KeyName` variable in
`PlayerPrefs.SetInt` as an identifier, and `Value` as the contents to store.
For example, you could use `PlayerPrefs.SetInt` to store the user’s currency,
like this: /PlayerPrefs.SetInt(“CharacterMoney”, 123)/.  
  
The GetInt function then uses the same `KeyName` variable to retrieve the
value stored in the `PlayerPrefs` data.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public void SetInt(string KeyName, int Value)
        {
            [PlayerPrefs.SetInt](PlayerPrefs.SetInt.html)(KeyName, Value);
        }  
      
        public int Getint(string KeyName)
        {
            return [PlayerPrefs.GetInt](PlayerPrefs.GetInt.html)(KeyName);
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

