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

# PropertyDatabase Constructor

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

public PropertyDatabase(string filePath);

### Parameters

filePath | Path to the backing file.  
---|---  
  
### Description

Constructs a new instance of a
[PropertyDatabase](Search.PropertyDatabase.html).

If **filePath** does not exist, the file will be created automatically. The
[PropertyDatabase](Search.PropertyDatabase.html) will not update the backing
file automatically, you will have to trigger the update manually with
[PropertyDatabase.TriggerBackgroundUpdate](Search.PropertyDatabase.TriggerBackgroundUpdate.html).
If another [PropertyDatabase](Search.PropertyDatabase.html) is already opened
on the same file, the [PropertyDatabase](Search.PropertyDatabase.html) will
not be opened and will be invalid. See [valid](Search.PropertyDatabase-
valid.html).

* * *

## Declaration

public PropertyDatabase(string filePath, bool autoFlush, double
backgroundUpdateDebounceInSeconds);

### Parameters

filePath | Path to the backing file.  
---|---  
autoFlush | Boolean indicating if the backing file will be updated automatically or not.  
backgroundUpdateDebounceInSeconds | Time between changes for the automatic background update to trigger.  
  
### Description

Constructs a new instance of a
[PropertyDatabase](Search.PropertyDatabase.html).

If **filePath** does not exist, the file will be created automatically. If
**autoBackgroundUpdate** is true, the
[PropertyDatabase](Search.PropertyDatabase.html) will automatically update the
backing file after changes have completed. To prevent updating the file too
often when there is a lot of changes, you can specify a delay between changes
with **backgroundUpdateDebounceInSeconds** before the update can trigger. For
example, with the default value of 5 seconds, a background update will only
happen after 5 seconds have passed since the last changes to the
[PropertyDatabase](Search.PropertyDatabase.html). If another
[PropertyDatabase](Search.PropertyDatabase.html) is already opened on the same
file, the [PropertyDatabase](Search.PropertyDatabase.html) will not be opened
and will be invalid. See [valid](Search.PropertyDatabase-valid.html).

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

