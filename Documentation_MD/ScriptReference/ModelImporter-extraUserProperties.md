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

#  [ModelImporter](ModelImporter.html).extraUserProperties

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

public string[] extraUserProperties;

### Description

A list of default FBX properties to treat as user properties during
OnPostprocessGameObjectWithUserProperties.

Specify the names of default FBX properties to be consider as extra user
properties to pass to
[AssetPostprocessor.OnPostprocessGameObjectWithUserProperties](AssetPostprocessor.OnPostprocessGameObjectWithUserProperties.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class MyPostProcessor : [AssetPostprocessor](AssetPostprocessor.html)
    {
        public override uint GetVersion() => 1;  
      
        //Adding 1 FBX default properties to be considered as UserProperties + 1 not existing in the imported FBX
        private void OnPreprocessModel()
        {
            string[] extraUserPropertyNames =
            {
                "currentUVSet",
                "MyNonFbxDefaultProperty"
            };
            (([ModelImporter](ModelImporter.html))assetImporter).extraUserProperties = extraUserPropertyNames;
        }  
      
        //Importing a FBX with a user defined Property "MyDefinedProperty"
        private void OnPostprocessGameObjectWithUserProperties([GameObject](GameObject.html) go, string[] propNames, object[] values)
        {
            foreach (var propName in propNames)
            {
                [Debug.Log](Debug.Log.html)(propName);
            }
        }  
      
        // Will display :
        //  currentUVSet
        //  MyDefinedProperty
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

