Data: -
    n_features = 
    m_instances = 70,000
    time_range = doesn't matter but data of last 2 years used (post covid data)
    granularity = hcp_level

Tables: -
    account
        id, name, address, designation, 
        gender, 
        consent_given, 
        key_opinion_leader? -> doctor, professor, key_opinion_leader
    calls
        call_duration
        f2f, 
        remote, 
        group
    emails
        sent, 
        opened,
        clicked,
    events
        newsletter_sent, 
        event_attended
    
Data cleaning:
    missing values
    x outliers
    x scaling 

Algorithm
    k_means -> 8 clusters
    elbow graph
    silhoutte score
