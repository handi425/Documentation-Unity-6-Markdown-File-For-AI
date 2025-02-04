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

#  [AssetDatabase](AssetDatabase.html).AddObjectToAsset

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

public static void AddObjectToAsset([Object](Object.html) objectToAdd, string
path);

### Parameters

objectToAdd | Object to add to the existing asset.  
---|---  
path | Filesystem path to the destination asset.  
  
### Description

Adds `objectToAdd` to an existing asset at `path`.

Please note that you should only add objects to '.asset' assets, imported
models or texture objects for example will lose their data.  
  
All paths are relative to the project folder.  
  
**Note:** You can not add GameObjects; use [PrefabUtility](PrefabUtility.html)
instead.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class AddObjectToAssetPathExample
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/AddObjectToAssetPathExample")]
        static void AddObjectToPathExample()
        {
            // Create a simple material object
            [Material](Material.html) material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Specular"));
            material.name = "My material";  
      
            // Create an instance of a simple scriptable object
            DummyObject dummyObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<DummyObject>();
            dummyObject.name = "My scriptable asset";  
      
            // Create the scriptable object asset
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(dummyObject, "Assets/dummyObject.asset");  
      
            // Get the path of the scriptable object asset
            string dummyObjectPath = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(dummyObject);  
      
            // Add the material to the scriptable object asset
            [AssetDatabase.AddObjectToAsset](AssetDatabase.AddObjectToAsset.html)(material, dummyObjectPath);  
      
            // Serializing the changes in memory to disk
            [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html)();  
      
            // Print the path of the created asset
            [Debug.Log](Debug.Log.html)([AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(dummyObject));
        }
    }  
      
    // The DummyObject class used in the example above
    public class DummyObject : [ScriptableObject](ScriptableObject.html)
    {
        public string objectName = "dummy";
    }
    

* * *

## Declaration

public static void AddObjectToAsset([Object](Object.html) objectToAdd,
[Object](Object.html) assetObject);

### Parameters

objectToAdd | Object to add to the existing asset.  
---|---  
assetObject | Destination asset.  
  
### Description

Adds `objectToAdd` to an existing asset identified by `assetObject`.

**Note:** Having `objectToAdd` on disc before calling AddObjectToAsset will
generate an error (ex. trying to add "MyMaterial" to an existing asset):
"Couldn't add object to asset file because the Material 'MyMaterial' is
already an asset at 'Assets/MyMaterial.mat'!"  
  
**Note:** You have to serialize the changes in memory to disk.  
This is because assets that have been modified in memory, must be saved to
disk.  
Failling to do this will produce an inconsistent result warning, as in-memory
modifications to the asset will be lost.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class AddObjectToAssetExample
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/AddObjectExample")]
        static void AddObjectExample()
        {
            // Create a simple material object
            [Material](Material.html) material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Specular"));
            material.name = "My material";  
      
            // Create an instance of a simple scriptable object
            DummyObject dummyObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<DummyObject>();
            dummyObject.name = "My scriptable asset";  
      
            // Create the scriptable object asset
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(dummyObject, "Assets/dummyObject.asset");  
      
            // Add the material to the scriptable object asset
            [AssetDatabase.AddObjectToAsset](AssetDatabase.AddObjectToAsset.html)(material, dummyObject);  
      
            // Serializing the changes in memory to disk
            [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html)();  
      
            // Print the path of the created asset
            [Debug.Log](Debug.Log.html)([AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(dummyObject));
        }
    }  
      
    // The DummyObject class used in the example above
    public class DummyObject : [ScriptableObject](ScriptableObject.html)
    {
        public string objectName = "dummy";
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

