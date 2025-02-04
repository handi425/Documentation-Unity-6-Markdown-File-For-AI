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

# PlistElementDict

class in UnityEditor.iOS.Xcode

/

Inherits from:[iOS.Xcode.PlistElement](iOS.Xcode.PlistElement.html)

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

Represents a dictionary element in plist document.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;  
      
    public class PlistDocumentExample
    {
        [PostProcessBuild]
        public static void PlistDocumentAPIExample([BuildTarget](BuildTarget.html) buildTarget, string pathToBuiltProject)
        {
            if (buildTarget == [BuildTarget.iOS](BuildTarget.iOS.html)) 
            {
                // Read the contents of the Info.plist file that was generated during the build
                string plistPath = pathToBuiltProject + "/Info.plist";
                [PlistDocument](iOS.Xcode.PlistDocument.html) plist = new [PlistDocument](iOS.Xcode.PlistDocument.html)();
                plist.ReadFromFile(plistPath);
        
                // Get root plist element
                [PlistElementDict](iOS.Xcode.PlistElementDict.html) rootDict = plist.root;  
      
                // Use helper methods such as SetBoolean, SetInteger or SetDate to modify or create new Info.plist entries
                // If a specified key doesn't already exist in the Info.plist, a new entry will be created
                rootDict.SetBoolean("ExampleBoolean", true);
                rootDict.SetInteger("ExampleInteger", 10);
                rootDict.SetDate("ExampleDate", DateTime.Today);  
      
                // Write the changes to the Info.plist file
                plist.WriteToFile(plistPath);
            }
        }
    }
    

### Properties

[this[string]](iOS.Xcode.PlistElementDict.Index_operator.html)| Convenience
method to access the stored values.  
---|---  
[values](iOS.Xcode.PlistElementDict-values.html)| The values stored in the
dictionary element.  
  
### Constructors

[PlistElementDict](iOS.Xcode.PlistElementDict-ctor.html)| Creates new
dictionary element.  
---|---  
  
### Public Methods

[CreateArray](iOS.Xcode.PlistElementDict.CreateArray.html)| Convenience method
to set a property to a new array element.  
---|---  
[CreateDict](iOS.Xcode.PlistElementDict.CreateDict.html)| Convenience method
to set a property to a new dictionary element.  
[SetBoolean](iOS.Xcode.PlistElementDict.SetBoolean.html)| Convenience method
to set a boolean property.  
[SetDate](iOS.Xcode.PlistElementDict.SetDate.html)| Convenience method to set
a date property.  
[SetInteger](iOS.Xcode.PlistElementDict.SetInteger.html)| Convenience method
to set an integer property.  
[SetReal](iOS.Xcode.PlistElementDict.SetReal.html)| Convenience method to set
an real property.  
[SetString](iOS.Xcode.PlistElementDict.SetString.html)| Convenience method to
set a string property.  
  
### Inherited Members

### Properties

[this[string]](iOS.Xcode.PlistElement.Index_operator.html)| Convenience method
to access properties of a dictionary element.  
---|---  
  
### Public Methods

[AsArray](iOS.Xcode.PlistElement.AsArray.html)| Convenience function to
convert to array element.  
---|---  
[AsBoolean](iOS.Xcode.PlistElement.AsBoolean.html)| Convenience function to
convert to bool.  
[AsDate](iOS.Xcode.PlistElement.AsDate.html)| Convenience function to convert
to date.  
[AsDict](iOS.Xcode.PlistElement.AsDict.html)| Convenience function to convert
to dictionary element.  
[AsInteger](iOS.Xcode.PlistElement.AsInteger.html)| Convenience function to
convert to integer.  
[AsReal](iOS.Xcode.PlistElement.AsReal.html)| Convenience function to convert
to float.  
[AsString](iOS.Xcode.PlistElement.AsString.html)| Convenience function to
convert to string.  
  
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

