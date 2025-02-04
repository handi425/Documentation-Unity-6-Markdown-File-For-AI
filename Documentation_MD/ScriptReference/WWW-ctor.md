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

**Method group is Obsolete**  

# WWW Constructor

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

**Obsolete** Use UnityWebRequest, a fully featured replacement which is more
efficient and has additional features.

## Declaration

public WWW(string url);

### Parameters

url | The url to download. Must be '%' escaped.  
---|---  
  
### Returns

**void** A new WWW object. When it has been downloaded, the results can be
fetched from the returned object.

### Description

Creates a WWW request with the given URL.

This function creates and sends a GET request. The stream will automatically
start downloading the response.  
  
After the stream is created you have to wait for it to complete, then you can
access the downloaded data. As a convenience the stream can be yielded, so you
can very easily tell Unity to wait for the download to complete.  
  
**_Note:_** URL must be '%' escaped.

    
    
    // Get the latest webcam shot from outside "Friday's" in Times Square  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public string url = "https://images.earthcam.com/ec_metros/ourcams/fridays.jpg";
        IEnumerator Start()
        {
            // Start a download of the given URL
            using (WWW www = new WWW(url))
            {
                // Wait for download to complete
                yield return www;  
      
                // assign texture
                [Renderer](Renderer.html) renderer = GetComponent<[Renderer](Renderer.html)>();
                renderer.material.mainTexture = www.textureNonReadable;
            }
        }
    }
    

* * *

**Obsolete** Use UnityWebRequest, a fully featured replacement which is more
efficient and has additional features.

## Declaration

public WWW(string url, [WWWForm](WWWForm.html) form);

### Parameters

url | The url to download. Must be '%' escaped.  
---|---  
form | A [WWWForm](WWWForm.html) instance containing the form data to post.  
  
### Returns

**void** A new WWW object. When it has been downloaded, the results can be
fetched from the returned object.

### Description

Creates a WWW request with the given URL.

This function creates and sends a POST request with form data contained in a
[WWWForm](WWWForm.html) parameter. This is the same as calling `new
WWW(url,form.data, form.headers)`. The stream will automatically start
downloading the response.  
  
After the stream is created you have to wait for it to complete, then you can
access the downloaded data. As a convenience the stream can be yielded, so you
can very easily tell Unity to wait for the download to complete.  
  
**_Note:_** URL must be '%' escaped.

* * *

**Obsolete** Use UnityWebRequest, a fully featured replacement which is more
efficient and has additional features.

## Declaration

public WWW(string url, byte[] postData);

### Parameters

url | The url to download. Must be '%' escaped.  
---|---  
postData | A byte array of data to be posted to the url.  
  
### Returns

**void** A new WWW object. When it has been downloaded, the results can be
fetched from the returned object.

### Description

Creates a WWW request with the given URL.

This function creates and sends a POST request with raw post data contained in
postData. The stream will automatically start downloading the response. Use
this version if you need to post raw post data in a custom format to the
server.  
  
After the stream is created you have to wait for it to complete, then you can
access the downloaded data. As a convenience the stream can be yielded, so you
can very easily tell Unity to wait for the download to complete.  
  
**_Note:_** URL must be '%' escaped.

* * *

**Obsolete** This overload is deprecated. Use UnityEngine.WWW.WWW(string,
byte[], System.Collections.Generic.Dictionary<string, string>) instead.

## Declaration

public WWW(string url, byte[] postData, Hashtable headers);

### Parameters

url | The url to download. Must be '%' escaped.  
---|---  
postData | A byte array of data to be posted to the url.  
headers | A hash table of custom headers to send with the request.  
  
### Returns

**void** A new WWW object. When it has been downloaded, the results can be
fetched from the returned object.

### Description

Creates a WWW request with the given URL.

This function creates and sends a POST request with raw post data contained in
postData and custom request headers supplied in the `headers` hashtable. The
stream will automatically start downloading the response. Use this version if
you need to post raw post data in a custom format to the server or if you need
to supply custom request headers.  
  
After the stream is created you have to wait for it to complete, then you can
access the downloaded data. As a convenience the stream can be yielded, so you
can very easily tell Unity to wait for the download to complete.  
  
**_Note:_** URL must be '%' escaped.

* * *

**Obsolete** Use UnityWebRequest, a fully featured replacement which is more
efficient and has additional features.

## Declaration

public WWW(string url, byte[] postData, Dictionary<string,string> headers);

### Parameters

url | The url to download. Must be '%' escaped.  
---|---  
postData | A byte array of data to be posted to the url.  
headers | A dictionary that contains the header keys and values to pass to the server.  
  
### Returns

**void** A new WWW object. When it has been downloaded, the results can be
fetched from the returned object.

### Description

Creates a WWW request with the given URL.

This function creates and sends a POST request with raw post data contained in
postData and custom request headers supplied in the `headers` Dictionary. The
stream will automatically start downloading the response. Use this version if
you need to post raw post data in a custom format to the server or if you need
to supply custom request headers.  
  
After the stream is created you have to wait for it to complete, then you can
access the downloaded data. As a convenience the stream can be yielded, so you
can very easily tell Unity to wait for the download to complete.  
  
**_Note:_** URL must be '%' escaped.

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

