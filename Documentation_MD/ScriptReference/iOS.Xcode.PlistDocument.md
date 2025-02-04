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

# PlistDocument

class in UnityEditor.iOS.Xcode

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

Represents an Apple property list document. For more information on property
lists, refer to [Apple's
documentation](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-
CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44).

    
    
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

[root](iOS.Xcode.PlistDocument-root.html)| The root element of the property
list document.  
---|---  
[version](iOS.Xcode.PlistDocument-version.html)| The version of the property
list document. At the moment Apple uses '1.0' for all property list files.  
  
### Constructors

[PlistDocument](iOS.Xcode.PlistDocument-ctor.html)| Creates a new property
list document instance.  
---|---  
  
### Public Methods

[Create](iOS.Xcode.PlistDocument.Create.html)| Create a new property list
Document.  
---|---  
[ReadFromFile](iOS.Xcode.PlistDocument.ReadFromFile.html)| Reads the document
from a file identified by the given path.  
[ReadFromStream](iOS.Xcode.PlistDocument.ReadFromStream.html)| Reads the
project from the given text reader.  
[ReadFromString](iOS.Xcode.PlistDocument.ReadFromString.html)| Reads the
document from the given string.  
[WriteToFile](iOS.Xcode.PlistDocument.WriteToFile.html)| Writes the project
contents to the specified file.  
[WriteToStream](iOS.Xcode.PlistDocument.WriteToStream.html)| Writes the
document contents to the specified text writer.  
[WriteToString](iOS.Xcode.PlistDocument.WriteToString.html)| Writes the
document contents to a string.  
  
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

