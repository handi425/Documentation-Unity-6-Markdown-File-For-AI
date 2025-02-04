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

#  [AssetDatabase](AssetDatabase.html).GetTypeFromPathAndFileID

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

public static Type GetTypeFromPathAndFileID(string assetPath, long
localIdentifierInFile);

### Parameters

assetPath | The Asset's path.  
---|---  
localIdentifierInFile | The object's local file identifier.  
  
### Returns

**Type** The object's type.

### Description

Gets an object's type from an Asset path and a local file identifier.

The following script example shows how to get the types of a nested asset. A
material asset is added to a scriptable object asset (in this case called
DummyObject), and the types of these two assets are extracted by calling
GetTypeFromPathAndFileID.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class GetTypeFromPathAndFileIDExample
    {  
      
        // Create a menu item under the [GameObject](GameObject.html) menu.
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/GetTypeFromPathAndFileIDExample")]
        static void GetNestedType()
        {
            // Create a simple material object.
            [Material](Material.html) material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Specular"));
            material.name = "My material";  
      
            // Create an instance of a simple scriptable object
            DummyObject scriptableObject = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<DummyObject>();
            scriptableObject.name = "My scriptable object";  
      
            // Create the scriptable object asset
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(scriptableObject, "Assets/myScriptableObject.asset");  
      
            // Add the material to the scriptable object asset
            [AssetDatabase.AddObjectToAsset](AssetDatabase.AddObjectToAsset.html)(material, scriptableObject);
            [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html)();  
      
            // Get the path of the created asset
            string scriptableObjectPath = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(scriptableObject);  
      
            // Get the GUID and the local file identifier of the scriptable object and the material.
            string materialGUID, scriptableObjectGUID;
            long materialFileID, scriptableObjectFileID;
            [AssetDatabase.TryGetGUIDAndLocalFileIdentifier](AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)(scriptableObject, out scriptableObjectGUID, out scriptableObjectFileID);
            [AssetDatabase.TryGetGUIDAndLocalFileIdentifier](AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)(material, out materialGUID, out materialFileID);  
      
            // Print type, local file identifier and path of the two assets.
            // Notice that the nested assets has the same path as the parent but different local file identifier.
            [Debug.Log](Debug.Log.html)(scriptableObject.name+" type: "+ [AssetDatabase.GetTypeFromPathAndFileID](AssetDatabase.GetTypeFromPathAndFileID.html)(scriptableObjectPath, scriptableObjectFileID) + ", fileID: "+scriptableObjectFileID+", path: " + scriptableObjectPath);
            [Debug.Log](Debug.Log.html)(material.name+" type: "+ [AssetDatabase.GetTypeFromPathAndFileID](AssetDatabase.GetTypeFromPathAndFileID.html)(scriptableObjectPath, materialFileID) + ", fileID: " + materialFileID + ", path: " + scriptableObjectPath);
        }
    }  
      
    public class DummyObject : [ScriptableObject](ScriptableObject.html) {
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

