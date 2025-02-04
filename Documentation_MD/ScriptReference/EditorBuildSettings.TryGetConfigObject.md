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

#  [EditorBuildSettings](EditorBuildSettings.html).TryGetConfigObject

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

public static bool TryGetConfigObject(string name, out T result);

### Parameters

name | The name in string format of the config object reference to be fetched.  
---|---  
result | The config object reference where the returned object will be stored. This must be an object of type Object.  
  
### Returns

**bool** Returns true if the config object reference was found and the type
matched the result parameter. Returns false if the entry is not found, the
config object reference is `null`, or if the type requested does not match the
type stored.

### Description

Retrieve a config object reference by name.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.IO;  
      
    public class MyConfigData : [ScriptableObject](ScriptableObject.html)
    {
        public static MyConfigData GetDefault()
        {
            //name of config data object
            string stringName = "com.myproject.myconfigdata";
            //path to Config Object and asset name
            string stringPath = "Assets/myconfigdata.asset";
            //used to hold config data
            MyConfigData data = null;  
      
            //if a config data object exists with the same name, return its config data
            if ([EditorBuildSettings.TryGetConfigObject](EditorBuildSettings.TryGetConfigObject.html)<MyConfigData>(stringName, out data))
                return data;  
      
            //If the asset file already exists, store existing config data
            if ([File.Exists](Windows.File.Exists.html)(stringPath))
                data = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<MyConfigData>(stringPath);
            //if no previous config data exists
            if (data == null)
            {
                //show save file dialog and return user selected path name
                stringPath = [EditorUtility.SaveFilePanelInProject](EditorUtility.SaveFilePanelInProject.html)("New Config [File](Windows.File.html)", "myconfigdata", "asset", "Select Config [File](Windows.File.html) [Asset](VersionControl.Asset.html)", "Assets");
                //initialise config data object
                data = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<MyConfigData>();
                //create new asset from data at specified path
                //asset MUST be saved with the [AssetDatabase](AssetDatabase.html) before adding to [EditorBuildSettings](EditorBuildSettings.html)
                [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(data, stringPath);
            }  
      
            //add the new or loaded config object to [EditorBuildSettings](EditorBuildSettings.html)
            [EditorBuildSettings.AddConfigObject](EditorBuildSettings.AddConfigObject.html)(stringName, data, false);  
      
            return data;
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

